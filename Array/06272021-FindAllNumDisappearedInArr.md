# Find All Numbers Disappeared in an Array

## Description

* Given an array nums of n integers where nums[i] is in the range [1, n], return an array of all the integers in the range [1, n] that do not appear in nums.

## Solution

### Two-pass

* iterate through the input array and **mark the element nums[nums[i]-1] as negative**
* Time: O(n)
* Space: O(1)

### Java

* absolute: Math.abs()
