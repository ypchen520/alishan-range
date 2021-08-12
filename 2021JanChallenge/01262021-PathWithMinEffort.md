# Path With Minimum Effort

## Description

* You are a hiker preparing for an upcoming hike. You are given heights, a 2D array of size rows x columns, where heights[row][col] represents the height of cell (row, col). You are situated in the top-left cell, (0, 0), and you hope to travel to the bottom-right cell, (rows-1, columns-1) (i.e., 0-indexed). You can move up, down, left, or right, and you wish to find a route that requires the minimum effort.
* A route's effort is the maximum absolute difference in heights between two consecutive cells of the route.
* Return the minimum effort required to travel from the top-left cell to the bottom-right cell.

## Solution

### Hint

* Consider the grid as a graph, where adjacent cells have an edge with cost of the difference between the cells.
* If you are given threshold k, check if it is possible to go from (0, 0) to (n-1, m-1) using only edges of ≤ k cost.
* Binary search the k value.

### BFS

* This way is slower because of the need of going back and re-evaluate a route if found less effort from another path
* we need to keep track of an effort matrix
  * the effort value of each location

### Dijkstra

### Matrix

* DIR = [0, 1, 0, -1] (move up, down, left, or right)

### Python

* set of tuples
  * initialize
    * SET = set([(0,0)])
* set
  * Because sets **cannot have multiple occurrences of the same element**, it makes sets highly useful to efficiently remove duplicate values from a list or tuple and to perform common math operations like **unions and intersections**.
