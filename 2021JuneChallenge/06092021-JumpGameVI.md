# Jump Game VI

## Description

* You are given a 0-indexed integer array nums and an integer k.
* You are initially standing at index 0. In one move, you can jump at most k steps forward without going outside the boundaries of the array. That is, you can jump from index i to any index in the range [i + 1, min(n - 1, i + k)] inclusive.
* You want to reach the last index of the array (index n - 1). Your score is the sum of all nums[j] for each index j you visited in the array.
* Return the maximum score you can get.

## Solution

### Hint

* Let dp[i] be "the maximum score to reach the end starting at index i". The answer for dp[i] is nums[i] + min{dp[i+j]} for 1 <= j <= k. That gives an O(n*k) solution.
* Instead of checking every j for every i, keep track of the smallest dp[i] values in a heap and calculate dp[i] from right to left. When the smallest value in the heap is out of bounds of the current index, remove it and keep checking.

### DP+Heap
