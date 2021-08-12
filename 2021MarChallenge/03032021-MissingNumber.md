# Missing Number

## Description

* Given an array nums containing n distinct numbers in the range [0, n], return the only number in the range that is missing from the array.
* **Follow up**: Could you implement a solution using only O(1) extra space complexity and O(n) runtime complexity?

## Solution

### Sorting

### HashSet

### Gauss' Formula

* expected sum: n(n+1)*2
* actual sum

  ```java
  for(int i : nums) actualSum += nums[i];
  ```
  
* answer = expected sum - actual sum
* time complexity: O(n)
* space complexity: O(1)

### Bitwise operation

* XOR
  * Java: ^
  * within a for-loop, perform the XOR operation on both the index i and nums[i].

### Indexing

* nums[nums[i]]
