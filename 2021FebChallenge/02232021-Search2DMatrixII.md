# Search a 2D Matrix II

## Description

* Write an efficient algorithm that searches for a target value in an m x n integer matrix. The matrix has the following properties:
  * Integers in each row are sorted in ascending from left to right.
  * Integers in each column are sorted in ascending from top to bottom.

## Solution

### Divide and Conquer

### O(n)

```python
i = 0
j = len(mat[0]) - 1
while i < len(mat) and j >= 0:
```
