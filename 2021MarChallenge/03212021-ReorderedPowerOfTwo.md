# Reordered Power of 2

## Description

* Starting with a positive integer N, we reorder the digits in any order (including the original order) such that the leading digit is not zero.
* Return true if and only if we can do this in a way such that the resulting number is a power of 2.

## Solution

* map all the digits to the power of 10
  * E.g., map 46 to 10<sup>4</sup> + 10<sup>6</sup> = 1010000
  * this way the digits are automatically reordered (i.e., 16 and 61 will have the same result from the mapping)
