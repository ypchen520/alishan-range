# [Max Consecutive Ones II](https://cheonhyangzhang.gitbooks.io/leetcode-solutions/content/solutions-451-500/487-max-consecutive-ones-ii.html)

## Description

* Given a binary array, find the maximum number of consecutive 1s in this array if you can flip at most one 0.

## Solution

### Two-pointer

* Flipped
  * if 0 is encountered, flip it, Flipped ```Flipped``` = ```notFlipped```+1
* notFlipped
  * if 0 is not encountered, keep adding to it
  * if 0 is encountered, reset to 0
* for each loop
  * compare the current maximum ```res``` and ```Flipped``` + ```notFlipped```
  