
```python
import collections
import heapq

class Twitter(object):

    def __init__(self):
        self.tweetMap = collections.defaultdict(collections.deque)
        self.following = collections.defaultdict(set)
        self.globalCount = 0
        
    def postTweet(self, userId, tweetId):
        self.globalCount += 1
        self.tweetMap[userId].appendleft((self.globalCount, tweetId))
        if len(self.tweetMap[userId]) > 10:
            self.tweetMap[userId].pop()

    def getNewsFeed(self, userId):
        heap = []
        def accumulate_tweets(tweet):
            heapq.heappush(heap, tweet)
            if len(heap) > 10:
                heapq.heappop(heap)
        
        for tweet in self.tweetMap[userId]:
            accumulate_tweets(tweet)
        
        for followee in self.following[userId]:
            tweetList = self.tweetMap[followee]
            for tweet in tweetList:
                accumulate_tweets(tweet)
                
        heap.sort(reverse=True)
        
        return [tweet[1] for tweet in heap]
        
    def follow(self, followerId, followeeId):
        self.following[followerId].add(followeeId)

    def unfollow(self, followerId, followeeId):
        self.following[followerId].discard(followeeId)


twitter = Twitter() 
twitter.postTweet(1, 5)
print(twitter.getNewsFeed(1))
twitter.follow(1, 2)
twitter.postTweet(2, 6)
print(twitter.getNewsFeed(1))
```
