# Reshape the Matrix

## Description

* In MATLAB, there is a handy function called reshape which can reshape an m x n matrix into a new one with a different size r x c keeping its original data.
* You are given an m x n matrix mat and two integers r and c representing the row number and column number of the wanted reshaped matrix.
* The reshaped matrix should be filled with all the elements of the original matrix in the same row-traversing order as they were.
* If the reshape operation with given parameters is possible and legal, output the new reshaped matrix; Otherwise, output the original matrix.

## Solution

### Hint

* Do you know how 2d matrix is stored in 1d memory? Try to map 2-dimensions into one.
* M[i][j]=M[n*i+j] , where n is the number of cols. This is the one way of converting 2-d indices into one 1-d index. Now, how will you convert 1-d index into 2-d indices?
* Try to use division and modulus to convert 1-d index into 2-d indices.
* M[i] => M[i/n][i%n] Will it result in right mapping? Take some example and check this formula.

### Java

* matrix
  * int[][] mat
    * mat.length (m): number of rows (size of a column)
    * mat[i].length (n): number of columns (size of a row)
  * 2D to 1D: M[i][j]=M[n*i+j]
  * 1D to 2D: M[i] => M[i/n][i%n]
