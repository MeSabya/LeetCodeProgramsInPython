# Cheapest Flights Within K Stops 

>There are n cities connected by some number of flights. You are given an array flights where flights[i] = [fromi, toi, pricei] indicates that there is a flight from city fromi to city toi with cost pricei.

>You are also given three integers src, dst, and k, return the cheapest price from src to dst with at most k stops. If there is no such route, return -1.

>Input: n = 3, flights = [[0,1,100],[1,2,100],[0,2,500]], src = 0, dst = 2, k = 1
Output: 200
Explanation: The graph is shown.
The cheapest price from city 0 to city 2 with at most 1 stop costs 200, as marked red in the picture.

![image](https://user-images.githubusercontent.com/33947539/149771981-fefaa2a1-3ad0-492e-8418-ac021e365a44.png)

 ```lua
 Algorithm:
 1. It is same as basic Dijkistras Algorithm. 
 2. In Dijkistras algorithm , we need to maintain smallest possible distance from source to every other node.
 3. Here we need to find out distance between source to destination , the minimum distance with a constraint of K stops.
 4.
 ```
 #### References:
 
 https://leetcode.com/problems/cheapest-flights-within-k-stops/discuss/362377/Dijkstra-Python-commented-and-explained
