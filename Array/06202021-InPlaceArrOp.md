# In-Place Array Operations Introduction

* In-place Array operations help to reduce space complexity
* The technique of working directly in the input Array, and not creating a new Array

## Replace Elements with Greatest Element on Right Side

### Description

* Given an array arr, replace every element in that array with the greatest element among the elements to its right, and replace the last element with -1.

### Solution

#### Hint

* Loop through the array starting **from the end**.
* Keep the maximum value seen so far.

#### Java

* Min/Max
  * Math.min/max
  * Integer.MIN/MAX_VALUE
  