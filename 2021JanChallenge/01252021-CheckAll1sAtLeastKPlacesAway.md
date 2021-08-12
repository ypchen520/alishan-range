# Check If All 1's Are at Least Length K Places Away

## Description

* Given an array nums of 0s and 1s and an integer k, return True if all 1's are at least k places away from each other, otherwise return False.

## Solution

### Hint

* Each time you find a number 1, check whether or not it is K or more places away from the next one. If it's not, return false.

### O(N) time Solution

* keep track of
  * index of the last 1
  * whether or not the 1 is the first one

### Bit Manipulation
