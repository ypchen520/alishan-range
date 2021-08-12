# Check If N and Its Double Exist

## Description

* Given an array arr of integers, check if there exists two integers N and M such that N is the double of M ( i.e. N = 2 * M)
* More formally check if there exists two indices i and j such that :
  * i != j
  * 0 <= i, j < arr.length
  * arr[i] == 2 * arr[j]

## Solution

### Hint

* Loop from i = 0 to arr.length, maintaining in a hashTable the array elements from [0, i - 1].
* On each step of the loop check if we have seen the element 2 * arr[i] so far or arr[i] / 2 was seen if arr[i] % 2 == 0.

### Hashtable

### Java

* [HashMap vs. Hashtable](https://www.geeksforgeeks.org/differences-between-hashmap-and-hashtable-in-java/)
* array length: arr.length
* string length: str.length()
