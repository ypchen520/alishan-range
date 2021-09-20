# Sum of Distances in Tree

## Description

* There is an undirected connected tree with n nodes labeled from 0 to n - 1 and n - 1 edges.
* You are given the integer n and the array edges where edges[i] = [ai, bi] indicates that there is an edge between nodes ai and bi in the tree.
* Return an array answer of length n where answer[i] is the sum of the distances between the ith node in the tree and all other nodes.

## Solution

### [Subtree Sum and Count](https://leetcode.com/problems/sum-of-distances-in-tree/solution/)

* We need to find out how ans[x] and ans[y] are related, so that we cut down on repeated work.
  * x and y are neighboring nodes (there is an edge between them)
  * subtree X
  * subtree Y
* ans[x] = x @ X + y @ Y + #(Y)
  * x @ X: sum of the distances from x to the subnodes in subtree X
  * y @ Y: sum of the distances from y to the subnodes in subtree Y
  * #(Y): number of subnodes in subtree Y
    * for each subnodes in subtree Y, we need to add 1 to connect x and y
* Pre-order and Post-order DFS
