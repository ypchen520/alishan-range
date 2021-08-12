# Stone Game

## Description

* Alex and Lee play a game with piles of stones. There are an even number of piles arranged in a row, and each pile has a positive integer number of stones piles[i]
* The objective of the game is to end with the most stones.  The total number of stones is odd, so there are no ties.
* Alex and Lee take turns, with Alex starting first.  Each turn, a player takes the entire pile of stones from either the beginning or the end of the row.  This continues until there are no more piles left, at which point the person with the most stones wins.
* Assuming Alex and Lee play optimally, return True if and only if Alex wins the game.

## Solution

### DP

* whenever Lee scores points, it deducts from Alex's score instead
* 2D array
  * dp(i,j): the largest score Alex can achieve where the piles remaining are piles[i], ..., piles[j]
    * we want to know what the value of **each position** of the game is
    * recursion: dp(i,j) = max(piles[i] + dp(i+1,j) + piles[j] + dp(i, j-1))
* Start playing with size = 2, 4, 6, ..., ```piles.length```

### Observation

* Always true
  * if Alex always picks piles that are at **even positions**, Lee can only pick piles that are at **odd positions**
  * if Alex always picks piles that are at **odd positions**, Lee can only pick piles that are at **even positions**
  * therefore, Alex is always the winner because:
    * if the sum of ```piles[even]``` > the sum of ```piles[odd]```, Alex picks piles that are at **even positions** and wins
    * if the sum of ```piles[odd]``` > the sum of ```piles[even]```, Alex picks piles that are at **odd positions** and wins
