# Beautiful Arrangement

## Description

* Suppose you have n integers from 1 to n
* if one of the following is true for the ith position (1 <= i <= n) in this array
  * The number at the ith position is divisible by i
  * i is divisible by the number at the ith position
* Given an integer n, return the number of the beautiful arrangements that you can construct

## Solution

* recursive
* backtracking
* A for-loop and recursion
  * for-loop
    * for each integer, we need to test it on all the positions that are not yet visited
  * recursion
    * when visiting a position with a specific start value, there will be two possible outcomes:
      * the value does not satisfy the requirement
        * no need to try the next value
      * the value satisfies the requirement
        * add one to the start value
        * mark the position as visited
        * call the function recursively with the new value
          * this value will visit the positions that are not yet visited
        * reset the visited flag for other possible combinations
          * the same start value but placed in a different position using the for-loop
