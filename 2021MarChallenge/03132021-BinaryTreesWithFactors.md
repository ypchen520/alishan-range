# Binary Trees With Factors

## Description

* Given an array of unique integers, arr, where each integer arr[i] is strictly greater than 1.
* We make a binary tree using these integers, and each number may be used for any number of times. Each non-leaf node's value should be equal to the product of the values of its children.
* Return the number of binary trees we can make. The answer may be too large so return the answer modulo 109 + 7.

## Solution

### Dynamic programming

* dp[8] = (dp[2] x dp[4]) + (dp[4] x dp[2])
* use unordered_map to keep track of the dp table
