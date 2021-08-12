# 3Sum Closest

## Description

* Given an array nums of n integers and an integer target, find three integers in nums such that the sum is closest to target. Return the sum of the three integers. You may assume that each input would have exactly one solution.

## Solution

### Two-pointer

* Sort the array
* one pointer i to iterate through the array
  * two pointer j and k at each i to search for the answer
* If current sum is less than the target
  * increase the left pointer
  * else decrease the right pointer
