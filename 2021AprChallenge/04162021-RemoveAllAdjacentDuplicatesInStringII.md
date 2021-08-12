# Remove All Adjacent Duplicates in String II

## Description

* You are given a string s and an integer k, a k duplicate removal consists of choosing k adjacent and equal letters from s and removing them, causing the left and the right side of the deleted substring to concatenate together.
* We repeatedly make k duplicate removals on s until we no longer can.
* Return the final string after all such duplicate removals have been made. It is guaranteed that the answer is unique.

## Solution

### C++

* pair

### Hint

* Use a stack to store the characters, when there are k same characters, delete them.
* To make it more efficient, use a pair to store the value and the count of each character.