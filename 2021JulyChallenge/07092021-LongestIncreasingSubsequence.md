# Longest Increasing Subsequence (LIS)

## Description

* Given an integer array nums, return the length of the longest strictly increasing subsequence.
* A subsequence is a sequence that can be derived from an array by deleting some or no elements without changing the order of the remaining elements. For example, [3,6,2,7] is a subsequence of the array [0,3,1,6,2,2,7].

## [Solution](https://cp-algorithms.com/sequences/longest_increasing_subsequence.html)

### DP

* Time complexity: O(n<sup>2</sup>)
* dp[i]: the length of the LIS ending with the element arr[i]
  * the answer will be the maximum value in dp[]

### DP and Binary Search

* Time complexity: O(nlogn)

### Java

* Filling an array
  * Arrays.fill(arr, VAL)
