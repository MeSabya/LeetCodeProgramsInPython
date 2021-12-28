# Union-Find Basics

*The union-find algorithm is one approach to solve the network connectivity problem, that is given a network, is there a path from one part of the network to another part? Take a friendship graph on Facebook for example, when Sarah goes on Rob’s page, the internal Facebook system will ask, do Sarah and Rob have mutual friends?*

![image](https://user-images.githubusercontent.com/33947539/147533967-58066f1e-ebb3-4b31-958b-79013fbd52cc.png)

We can look at this image and identify that people are the blue figurines, the red line indicates friendship, and since there is a path of friends from Sarah to Rob (via person C and then A), then we conclude that Sarah and Rob do have mutual friends. Mathematicians represent this information using sets. A set is a collection of items that can be organized together. The smallest of sets is an empty set, denoted by {}. The above figure can be represented by two sets, {A, Rob, Sarah, C} and {B, D}. We notice that these two sets do not share any of the same elements, thus they are called disjoint sets.

The union-find algorithm uses disjoint data sets to solve the network connectivity problem. This algorithm has three operations it can call:

✔ Union : Given two nodes u and v, to merge them together if they’re disjoint. Otherwise, return False, which means they’re connected already.

✔ Find(): Given a node u, to find root node of u. Determine which subset a particular element is in. This can be used for determining if two elements are in the same subset.

✔ Makeset(E): Create a new subset with the element E.

Let us work this out in on the previous example. We start out with subsets [{A}, {Rob}, {Sarah}, {C}, {B}, {D}] by calling Makeset 6 times. Then we see that Rob is connected to A directly, so we call Union({Rob}, {A}), since both subsets are the same size, we arbitrarily let Rob be the representative so we have {Rob, A}. We also see that C is connected to A, so we call Union({Rob, A}, {C}). We continue doing this until we have the two disjoint sets {Rob, A, C, Sarah} and {B, D}. Now the Find operation is easy because we can call Find(Rob) and Find(Sarah) who both return the same representative element, Rob, leading us to conclude that they are in the same set, thus are connected by mutual friends.

## Applications:
1. connected component in Graph problem

2. detecting cycles in an undirected graph.

3. minimum spanning tree

## Defination:
A Union-Find data structure also called Disjoint set data structure is to maintain a set of elements partitioned into a number of mutually disjoint(non-overlapping) subsets. So, no elements belong to more than one set.

### References:
- https://www.geeksforgeeks.org/union-find/
