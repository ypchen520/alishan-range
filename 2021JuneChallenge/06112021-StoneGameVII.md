# Stone Game VII

## Description

* Alice and Bob take turns playing a game, with Alice starting first.
* There are n stones arranged in a row. On each player's turn, they can remove either the leftmost stone or the rightmost stone from the row and receive points equal to the sum of the remaining stones' values in the row. The winner is the one with the higher score when there are no stones left to remove.
* Bob found that he will always lose this game (poor Bob, he always loses), so he decided to minimize the score's difference. Alice's goal is to maximize the difference in the score.
* Given an array of integers stones where stones[i] represents the value of the ith stone from the left, return the difference in Alice and Bob's score if they both play optimally.

## Solution

### Hint

* The constraints are small enough for an N^2 solution.
* Try using dynamic programming.

### [DP](https://leetcode.com/problems/stone-game-vii/discuss/1264516/JS-Python-Java-C%2B%2B-or-Easy-DP-Solution-w-Explanation)

* dp[i][j] would represent **the best score difference** with
  * i representing the leftmost remaining stone's index and
  * j representing the rightmost remaining stone's index
* top-down
  * start at i = N - 2 and iterate backwards and start each nested for loop at j = i + 1
  * we're building the pyramid of DP results downward
* For each row
  * we'll keep track of **the sum total of the stones in the range [i,j]** by adding S[j] at each iteration of j
  * we can represent the current player's ideal play by choosing the best value between picking the stone at i (total - S[i]) and picking the stone at j (total - S[j])
    * For each option, we have to also subtract the best value that the other player will get from the resulting board position (dp[i+1][j] or dp[i][j-1])
* Since we will only be building off the current and previously-finished rows, however, we can actually eliminate the DP matrix and instead just define two N-length arrays representing the current and previous rows (dpCurr, dpLast), and swap between them at each iteration of i. This will drop the space complexity from O(N^2) to O(N)
