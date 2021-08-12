# Find the Most Competitive Subsequence

## Description

* Given an integer array nums and a positive integer k, return the most competitive subsequence of nums of size k.
* An array's subsequence is a resulting sequence obtained by erasing some (possibly zero) elements from the array.
* We define that a subsequence a is more competitive than a subsequence b (of the same length) if in the first position where a and b differ, subsequence a has a number less than the corresponding number in b. 
  * For example, [1,3,4] is more competitive than [1,3,5] because the first position they differ is at the final number, and 4 is less than 5.

## Solution

### Hint

* In lexicographical order, the elements to the left have higher priority than those that come after. Can you think of a strategy that incrementally builds the answer from left to right?

### Use a Stack

* Use a stack to track the best solution so far
* pop if the current number is less than the top of the stack and there are sufficient numbers left
* Then push the current number to the stack if not full
* Time complexity: O(n)
* Space complexity: O(k)
