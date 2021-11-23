# Shortest Path in a Grid with Obstacles Elimination

## Description

* You are given an m x n integer matrix grid where each cell is either 0 (empty) or 1 (obstacle). You can move up, down, left, or right from and to an empty cell in one step.
* Return the minimum number of steps to walk from the upper left corner (0, 0) to the lower right corner (m - 1, n - 1) given that you can eliminate at most k obstacles. If it is not possible to find such walk return -1.

## Solution

### Hint

* Use BFS
* BFS on (x,y,r) x,y is coordinate, r is remain number of obstacles you can remove.

### BFS

```Java
int[][] dirs = new int[][]{{0,1},{0,-1},{1,0},{-1,0}};
```

### Java

* Queue<> q = new LinkedList<>();
* q.offer (q.add)
* q.poll()
