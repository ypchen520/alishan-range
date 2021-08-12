# Arithmetic Slices

## Description

* A sequence of numbers is called arithmetic if it consists of at least three elements and if the difference between any two consecutive elements is the same.
* A zero-indexed array A consisting of N numbers is given. A slice of that array is any pair of integers (P, Q) such that [0 <= P < Q < N].
* A slice (P, Q) of the array A is called arithmetic if the sequence: A[P], A[P + 1], ..., A[Q - 1], A[Q] is arithmetic. In particular, this means that [P + 1 < Q].
* The function should return the number of arithmetic slices in the array A.

## Solution

* For each group of arithmetic sequences, compute the number of arithmetic slices and then add them up.
* Not a dynamic programming solution
* We can keep track of consecutive arithmetic triplets
  * and compute the permutation
  * since the sequence has to be consecutive
    * the number of sequences goes down by 1 when the length of the sequence increase by one
      * thus, we can use the trapezoid formula: (c+1) * c / 2
* E.g., 1,2,3,4,5
  * we have 3 sequences with the minimum length 3: (1,2,3), (2,3,4), (3,4,5)
  * and then 2 sequences with the minimum length 4: (1,2,3,4), (2,3,4,5)
  * and so on
  * so we can use the formula for 3 + 2 + 1 = (3+1)*3/2
