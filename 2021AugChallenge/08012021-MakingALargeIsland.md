# Making A Large Island

## Description

* You are given an n x n binary matrix grid. You are allowed to change at most one 0 to be 1.
* Return the size of the largest island in grid after applying this operation.
* An island is a 4-directionally connected group of 1s.

## Solution

### [DFS](https://www.cnblogs.com/grandyang/p/11669063.html)

* change each 0 to 1 and use DFS to find the largest island connected to the changed 0
* DFS
  * need to create an extra array ```visited```
  * the helper function returns the size of the island
    * 1 + helper(i-1, j) + helper(i, j-1) + helper(i+1, j) + helper(i, j+1)

### DFS + HashMap

* give an ID to each island
  * instead of using the ```visited``` array, we can change the grid element to the ID directly
  * start from ID = 2 to avoid the case where ID = 1
* use a HashMap to store the size of the island corresponding to the ID
* iterate through the grid again and check each 0 element's neighbor
  * use set to avoid checking the same island (with the same ID)
  