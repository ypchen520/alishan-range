# Sort the Matrix Diagonally

## Description

* A matrix diagonal is a diagonal line of cells starting from some cell in 
  * either the topmost row or 
  * leftmost column and going in the bottom-right direction 
  * until reaching the matrix's end. 
    * For example, the matrix diagonal starting from mat[2][0], where mat is a 6 x 3 matrix, includes cells mat[2][0], mat[3][1], and mat[4][2].

* Given an m x n matrix mat of integers, sort each matrix diagonal in ascending order and return the resulting matrix.

## Solution

### Hint

* Use a data structure to store all values of each diagonal.
* How to index the data structure with the id of the diagonal?
* All cells in the same diagonal (i,j) have the same difference so we can get the diagonal of a cell using the difference i-j.

### Diagonal

* get the diagonal of each column for the first row
* sort the diagonal and put back into the matrix diagonal
* get the diagonal of each row for the first column
* sort the diagonal and put back into the matrix diagonal
