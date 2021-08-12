# Flip String to Monotone Increasing

## Description

* A binary string is monotone increasing if it consists of some number of 0's (possibly none), followed by some number of 1's (also possibly none).
* You are given a binary string s. You can flip s[i] changing it from 0 to 1 or from 1 to 0.

## Solution

### Prefix Sums

* how many **ones** are in the left half, and how many **zeros** are in the right half
* prefix sums
  * calculate p[i]
    * p[i+1] = A[0] + A[1] + ... + A[i]
      * A[i] = 1 if S[i] == 1 else A[i] = 0
  * p[x]
    * number of ones in the range: 0 ... x-1 (inclusive)
    * flip p[x] will give us x zeros (in the left half)
  * Among the rest N-x elements
    * p[N]: number of all ones in the binary string
      * p[N] - p[x]: number of ones in the range x ... N-1 (inclusive)
    * flip (N-x) - (p[N] - p[x]) will give us N-x ones (in the right half)
  * number of total flips for a possible candidate
    * flip ones (in the left half): p[x]
    * flip zeros (in the right half): (N-x) - (p[N] - p[x])
