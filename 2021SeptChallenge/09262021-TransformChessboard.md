# Transform to Chessboard

## Description

* You are given an n x n binary grid board. In each move, you can swap any two rows with each other, or any two columns with each other.
* Return the minimum number of moves to transform the board into a chessboard board. If the task is impossible, return -1.
* A chessboard board is a board where no 0's and no 1's are 4-directionally adjacent.

## [Solution](https://leetcode.com/problems/transform-to-chessboard/discuss/132113/Java-Clear-Code-with-Detailed-Explanations)

* Half of the row (or column) are ones
* there are only two kinds of rows (or columns)
  * a row and its opposite
* 4 corners
  * 4 zeros
  * 4 ones
  * 2 zeros and 2 ones
