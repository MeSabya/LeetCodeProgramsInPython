## Problem Description

***Build a key-value data structure that allows the user to take a snapshot of the data. The user can read the key-value store from any snapshot.***

Structure has the normal key/value like methods plus something like

snapshot = dataStructure.takeSnapshot();
value = dataStructure.get(key, snapshot);
void dataStructure.deleteSnapshot();

```yaml
kv = KeyValueStore()
kv.putValue("a", 1)
kv.putValue("b", 2)

sid1 = kv.takeSnapshot()

kv.putValue("a", 3)
print(f'a sid1: {kv.getKey("a", sid1)}')
kv.putValue("b", 4)
kv.putValue("b", 5)
kv.putValue("b", 6)

sid2 = kv.takeSnapshot()

print(f'a sid1: {kv.getKey("a", sid1)}')
print(f'a sid2: {kv.getKey("a", sid2)}')
print(f'b sid1: {kv.getKey("b", sid1)}')
print(f'b sid2: {kv.getKey("b", sid2)}')

sid3 = kv.takeSnapshot()

print(f'b sid3: {kv.getKey("b", sid3)}')
```
The same key can be present in multiple snapshots and user can read the key from any snapshots. Constraint is our getKey(key, snapID) method should return the value associated with the key in 
the snaID. If snapID is not present then we should return the value in the previous snapID which is smaller to the given snapID.

```python
import threading
from collections import defaultdict
from threading import Event, RLock


class KeyValueStore():
    def __init__(self):
        self.store = defaultdict(list)
        self.storeSnapIndex = defaultdict(dict)
        self.snapID = 0
        self.snapshotInProgress = Event()
        self.snapshotLock = RLock()

    def _putValue(self, key: str, value: int):
        """
            maintains 2 data structures:
                * a map of keys to list of tuples (snapID, value)
                * a double map of keys -> snapID -> index in the key's snapshot list above
            if a key is being updated for same snapshot, pops the end of it's snapshot list first
            so that only one value is stored for one key, snapID
            O(1) operation
        """
        if key in self.store:
            if self.store[key][-1][0] == self.snapID:
                self.store[key].pop(-1)
        self.store[key].append((self.snapID, value))
        self.storeSnapIndex[key][self.snapID] = len(self.store[key])-1

    def putValue(self, key: str, value: int):
        """
            makes sure putValue's wait for any currently running snapshot operation
        """
        if self.snapshotInProgress.is_set():
            with self.snapshotLock:
                self._putValue(key, value)
        else:
            self._putValue(key, value)

    def binarySearch(self, snapVals, snapID):
        left = 0
        right = len(snapVals) - 1

        while left < right:
            mid = int((left + right) / 2)
            if snapVals[mid][0] < snapID:
                # go right half
                left = mid + 1
            elif snapVals[mid][0] > snapID:
                # go left half
                right = mid
            else:
                return snapVals[mid]
        return snapVals[left]

    def getKey(self, key: str, snapID: int):
        """
        O(1) in the best case
        O(logN) in the average case
        O(N) in the worse case

        where N = maximum snapshots for any key
        """
        if key in self.store:
            snapVals = self.store[key]
            # first checks if the requested snapID exists for this key
            # then return's its value by looking up that index in the snapshot list
            # for this key
            if snapID in self.storeSnapIndex[key]:
                return snapVals[self.storeSnapIndex[key][snapID]][1]
            # otherwise does a binary search in the snapshot list for the closest
            # snapshot ID lesser than the requested one
            else:
                return self.binarySearch(snapVals, snapID)[1]

    def takeSnapshot(self):
        # takes a lock to prevent putKey's happening
        # to avoid recent conditions, while snapshot index is incremented
        with self.snapshotLock:
            self.snapshotInProgress.set()
            snapID = self.snapID
            self.snapID += 1
            self.snapshotInProgress.clear()
        return snapID


def client1(kv):
    kv.putValue("b", "7")

def client2(kv):
    kv.takeSnapshot()

def client3(kv):
    sid1 = kv.takeSnapshot()
    print(f'b: {kv.getKey("b", sid1)}')

if __name__ == '__main__':
    kv = KeyValueStore()
    kv.putValue("a", 1)
    kv.putValue("b", 2)
    sid1 = kv.takeSnapshot()
    kv.putValue("a", 3)
    print(f'a sid1: {kv.getKey("a", sid1)}')
    kv.putValue("b", 4)
    kv.putValue("b", 5)
    kv.putValue("b", 6)
    sid2 = kv.takeSnapshot()
    print(f'a sid1: {kv.getKey("a", sid1)}')
    print(f'a sid2: {kv.getKey("a", sid2)}')
    print(f'b sid1: {kv.getKey("b", sid1)}')
    print(f'b sid2: {kv.getKey("b", sid2)}')
    sid3 = kv.takeSnapshot()
    print(f'b sid3: {kv.getKey("b", sid3)}')
    
    '''
    c1 = threading.Thread(target=client1, args=(kv,))
    c2 = threading.Thread(target=client2, args=(kv,))
    c3 = threading.Thread(target=client3, args=(kv,))
    c1.start()
    c2.start()
    c3.start()
    c1.join()
    c2.join()
    c3.join()
    '''
```
snapshot.
