# Valid Sudoku

## Description

* Determine if a 9 x 9 Sudoku board is valid. Only the filled cells need to be validated according to the following rules:
  * Each row must contain the digits 1-9 without repetition.
  * Each column must contain the digits 1-9 without repetition.
  * Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without repetition.
* Note
  * A Sudoku board (partially filled) could be valid but is not necessarily solvable.
  * Only the filled cells need to be validated according to the mentioned rules.

## [Solution](https://leetcode.com/problems/valid-sudoku/solution/)

### Hash Set

* we can use hash sets to store the previously seen numbers in each row, column, and box.
  * Initialize a hash set for each row, column, and box
    * List of HashSets (3 lists and 27 hash sets)
      * rows
      * cols
      * boxes (index calculation)
* Time complexity: O(N<sup>2</sup>)
* Space complexity: O(N<sup>2</sup>) 

### Array of Fixed Length

* Initialize a 2D array of size N filled withr zeros for each row, column, and box
  * int[][] rows = new int[N][N]
  * int[][] cols = new int[N][N]
  * int[][] boxes = new int[N][N]
* Time complexity: O(N<sup>2</sup>)
* Space complexity: O(N<sup>2</sup>) 

### Bitmasking

* Time complexity: O(N<sup>2</sup>)
* Space complexity: O(N) 
