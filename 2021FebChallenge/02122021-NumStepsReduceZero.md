# Number of Steps to Reduce a Number to Zero

## Description

* Given a non-negative integer num, return the number of steps to reduce it to zero. If the current number is even, you have to divide it by 2, otherwise, you have to subtract 1 from it.

## Solution

### Hint

* Simulate the process to get the final answer.

### bit manipulation

* From right to left
* For any 0, it takes 1 step, which is divide by 2
* For any 1, it takes 2 step, which is substract 1 and then divide by 2
* E.g.,
  * 9 -> 1001
    * for the rightmost 1 -> substract 1 -> 1000 -> divide by 2 --> 100
    * for the rightmost 0 -> divide by 2 --> 10
    * for the rightmost 0 -> divide by 2 --> 1
    * for the rightmost 1 -> substract 1 -> 0 divide by 2 --> 0 (**an extra manipulation**)
* count('1') + len(s) **- 1**

### recursive
