# Array Nesting

## Description

* You are given an integer array nums of length n where nums is a permutation of the numbers in the range [0, n - 1].
* You should build a set s[k] = {nums[k], nums[nums[k]], nums[nums[nums[k]]], ... } subjected to the following rule:
  * The first element in s[k] starts with the selection of the element nums[k] of index = k.
  * The next element in s[k] should be nums[nums[k]], and then nums[nums[nums[k]]], and so on.
  * We stop adding right before a duplicate element occurs in s[k].
* Return the longest length of a set s[k].

## Solution

### Brute Force

* O(n<sup>2</sup>)

### Visited Array

* the elements in the current nesting shown by arrows form a cycle
* the same elements will be added to the current set irrespective of the first element chosen to be added to the set
* space complexity: O(n)

### Without Extra Space

* Since the range of the elements can only be between 1 to 20,000, we can put a very large integer value \text{Integer.MAX_VALUE} at the position which has been visited.
