# https://leetcode.com/problems/seat-reservation-manager/
import heapq
class SeatManager:

    def __init__(self, n: int):
        self.seats_list = list(range(1, n+1))               
        heapify(self.seats_list)
    def reserve(self) -> int:
        return heappop(self.seats_list)
    def unreserve(self, seatNumber: int) -> None:
        heappush(self.seats_list, seatNumber)
        


# Your SeatManager object will be instantiated and called as such:
# obj = SeatManager(n)
# param_1 = obj.reserve()
# obj.unreserve(seatNumber)