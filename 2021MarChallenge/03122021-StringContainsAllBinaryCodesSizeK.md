# Check If a String Contains All Binary Codes of Size K

## Description

* Given a binary string s and an integer k.
* Return True if every binary code of length k is a substring of s. Otherwise, return False.

## Solution

### Hint

* We need only to check all sub-strings of length k.
* The number of distinct sub-strings should be exactly 2^k.

### Size of HashSet

* store distinct substrings of size k to the HashSet
* compare with 2<sup>k