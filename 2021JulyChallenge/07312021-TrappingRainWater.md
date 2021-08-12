# Trapping Rain Water

## Description

* Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it can trap after raining.

## Solution

### DP

* left[i]: the maximum height on the left side of the ith bar
  * left[i] = max(left[i-1], height[i])
* right[i]: the maximum height on the right side of the ith bar
  * right[i] = max(right[i+1], height[i])
* Iterate through the array **from left to right** and **from right to left**
* The trapped water at height[i] is: min(left[i], right[i]) - height[i]
  * When calculating the trapped water, we can actually ignore the first bar and the last bar

### Two-pointer
