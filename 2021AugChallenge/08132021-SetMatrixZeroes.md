# Set Matrix Zeroes

## Description

* Given an m x n integer matrix matrix, if an element is 0, set its entire row and column to 0's, and return the matrix.
* You must do it in place.

## Solution

### Hint

* If any cell of the matrix has a zero we can record its row and column number using additional memory. But if you don't want to use extra memory then you can manipulate the array instead. i.e. simulating exactly what the question says.
* Setting cell values to zero on the fly while iterating might lead to discrepancies. What if you use some other integer value as your marker? There is still a better approach for this problem with 0(1) space.
* We could have used 2 sets to keep a record of rows/columns which need to be set to zero. But for an O(1) space solution, you can use one of the rows and and one of the columns to keep track of this information.
* We can use the first cell of every row and column as a flag. This flag would determine whether a row or column has been set to zero.
