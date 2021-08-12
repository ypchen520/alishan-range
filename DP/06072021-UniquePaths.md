# Unique Paths

## Description

* A robot is located at the top-left corner of a m x n grid (marked 'Start' in the diagram below).
* The robot can only move either down or right at any point in time. The robot is trying to reach the bottom-right corner of the grid (marked 'Finish' in the diagram below).
* How many possible unique paths are there?

## Solution

### DP

#### Bottom-up

#### Top-down (backtracking)

```Python
memo = defaultdict(list)
        
def backTracking(m, n):
    if not memo[(m, n)]:
        if m < 0 or n < 0:
            return 0

        if m == 0 or n == 0:
            return 1

        res =  backTracking(m - 1, n) + backTracking(m, n - 1)
        memo[(m, n)] = res
        return memo[(m, n)]
    else:
        return memo[(m, n)]



L = backTracking(m - 1, n - 1)
return L
```
