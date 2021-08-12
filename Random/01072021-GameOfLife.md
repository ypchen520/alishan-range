# Game of Life

## Description

* Any live cell with fewer than two live neighbors dies as if caused by under-population.
* Any live cell with two or three live neighbors lives on to the next generation.
* Any live cell with more than three live neighbors dies, as if by over-population.
* Any dead cell with exactly three live neighbors becomes a live cell, as if by reproduction.

## Solution

### O(mn) Space Solution

* the first approach could be as easy as having a copy of the board
* Make a copy of the original board which will remain unchanged throughout the process

### O(1) Space Solution

* We can use some dummy cell value to represent previous state of the cell along with the new changed value
* If the value of the cell was 1 originally but it has now become 0 after applying the rule, then we can change the value to -1
* utilize the sign and the dummy value
  * negative sign means dead (now)
  * 1 means the cell was alive: -1
  * 2 means the cell was dead: +2
* Not really O(1)? (Not using boolean)

### Clone the 3 rows that are needed

* Ruby
  * row_above = nil
  * current_row = nil
  * row_below = board[0].dup
