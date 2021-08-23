# Range Sum Query - Immutable

## Description

* Given an integer array nums, handle multiple queries of the following type:
  * Calculate the sum of the elements of nums between indices left and right inclusive where left <= right.
* Implement the NumArray class:
  * NumArray(int[] nums) Initializes the object with the integer array nums.
  * int sumRange(int left, int right) Returns the sum of the elements of nums between indices left and right inclusive (i.e. nums[left] + nums[left + 1] + ... + nums[right]).

## [Solution](https://leetcode.com/problems/range-sum-query-immutable/discuss/75190/My-java-3ms-solution)

* create an array to store the cumulative sum
* range[left,right] = sum[right] - sum[left-1]

## Mutable

### [Solution](https://leetcode.com/problems/range-sum-query-mutable/solution/)

#### Sqrt Decomposition

#### Segment Tree
