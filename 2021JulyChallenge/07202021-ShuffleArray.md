# Shuffle an Array

## Description

* Given an integer array nums, design an algorithm to randomly shuffle the array. All permutations of the array should be equally likely as a result of the shuffling.
* Implement the Solution class:
  * Solution(int[] nums) Initializes the object with the integer array nums.
  * int[] reset() Resets the array to its original configuration and returns it.
  * int[] shuffle() Returns a random shuffling of the array.

## [Solution](https://www.programcreek.com/2014/08/leetcode-shuffle-an-array-java/)

### Hint

* The solution expects that we always use the original array to shuffle() else some of the test cases fail.

### Java

* random

```Java
Random rand;
```

* copy an array
  * Arrays.copyOf(arr, arr.length)
  * arr.clone()

### Fisher-Yates Algorithm

* In the for-loop, the next range from which we select a random index will not include the most recently processed one.
* In the 1st iteration, selected a certain index x: 1/n
* In the 2nd iteration, selected a certain index x: n-1/n (x not selected in previous iteration) * 1/n-1 = 1/n
* and so on
