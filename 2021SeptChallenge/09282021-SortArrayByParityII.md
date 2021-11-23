# Sort Array By Parity II

## Description

* Given an array of integers nums, half of the integers in nums are odd, and the other half are even.
* Sort the array so that whenever nums[i] is odd, i is odd, and whenever nums[i] is even, i is even.
* Return any answer array that satisfies this condition.

## Solution

### Two-pointer

* keep track of the even indices and odd indices
  * start with i = 0, j = 1
