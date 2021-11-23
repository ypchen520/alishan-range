# Find All Duplicates in an Array

## Description

* Given an integer array nums of length n where all the integers of nums are in the range [1, n] and each integer appears once or twice, return an array of all the integers that appears twice.
* You must write an algorithm that runs in O(n) time and uses only constant extra space.

## Solution

### Marking

* use the elements (i.e., nums[i]-1) as indices
  * for example, for input array: [3,1,2,4,1]
    * check nums[2], nums[0], nums[1], nums[3], nums[0]
* mark the checked elements by **changing the sign from positive to negative**
  * when using the checked elements as indices, use Math.abs(nums[i])
  