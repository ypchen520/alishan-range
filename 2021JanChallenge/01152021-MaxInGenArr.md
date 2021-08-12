# Get Maximum in Generated Array

## Description

* You are given an integer n. An array nums of length n + 1 is generated in the following way:
  * nums[0] = 0
  * nums[1] = 1
  * nums[2 * i] = nums[i] when 2 <= 2 * i <= n
  * nums[2 * i + 1] = nums[i] + nums[i + 1] when 2 <= 2 * i + 1 <= n
* Return the maximum integer in the array nums

## Solution

* Try generating the array.
* Make sure not to fall in the base case of 0.
* Keep track of the maximum when generating the array

### JAVA

* array
  * allocating memory to array
    * int[] Arr = new int[NUM]
