# Global and Local Inversions

## Description

* We have some permutation A of [0, 1, ..., N - 1], where N is the length of A.
* The number of (global) inversions is the number of i < j with 0 <= i < j < N and A[i] > A[j].
* The number of local inversions is the number of i with 0 <= i < N and A[i] > A[i+1].
* Return true if and only if the number of global inversions is equal to the number of local inversions.

## Solution

### Hint

* Where can the 0 be placed in an ideal permutation? What about the 1?

### Backtrack

* Whether it is possible to find a global inversion that is not a partial inversion
* In order to distinguish it from the local inversion, we can't compare the two adjacent ones
* traverse the array from back to front, traverse to the third number to stop, and then maintain a minimum value in the range [i, n-1]
* each time compared with A[i - 2], if less than A[i - 2], indicating that this is a global inversion, and not a partial inversion, then we can return false directly
