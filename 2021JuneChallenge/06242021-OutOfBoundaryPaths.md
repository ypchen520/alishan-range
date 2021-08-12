# Out of Boundary Paths

## Description

* There is an m x n grid with a ball. The ball is initially at the position [startRow, startColumn]. You are allowed to move the ball to one of the four adjacent cells in the grid (possibly out of the grid crossing the grid boundary). You can apply at most maxMove moves to the ball.
* Given the five integers m, n, maxMove, startRow, startColumn, return the number of paths to move the ball out of the grid boundary. Since the answer can be very large, return it modulo 10<sup>9</sup> + 7.

## Solution

### DP

* if we can reach some position in x moves, we can reach all its adjacent positions in x+1 move
* we need to update the corresponding dp entry as dp[i][j] = dp[i-1][j] + dp[i+1][j] + dp[i][j-1] + dp[i][j+1] taking care of boundary conditions
  * **if we alter the dp array, now some of the entries will correspond to x-1 moves and the updated ones will correspond to x moves**
    * we make use of a temporary 2-D array temp to store the updated results for x moves, making use of the results obtained for dp array corresponding to x-1 moves