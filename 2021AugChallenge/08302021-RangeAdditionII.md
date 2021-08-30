# Range Addition II

## Description

* You are given an m x n matrix M initialized with all 0's and an array of operations ops, where ops[i] = [ai, bi] means M[x][y] should be incremented by one for all 0 <= x < ai and 0 <= y < bi.
* Count and return the number of maximum integers in the matrix after performing all the operations.

## Solution

### Find Minimum

* since the operations always start from the upper left corner, all the operations will overlap on the upper left corner
* we only need to find the overlapping of each operation
  * we can achieve this by finding the minimum of the row operations and the minimum of the column operations
  