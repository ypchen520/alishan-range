# Advantage Shuffle

## Description

* Given two arrays A and B of equal size, the advantage of A with respect to B is the number of indices i for which A[i] > B[i].
* Return any permutation of A that maximizes its advantage with respect to B.

## Solution

* Take the "smallest" unused number A[j] such that A[j] > B[i]
* if no number in A is larger than B[i], take the smallest number in A

### Java

* [TreeMap](https://www.geeksforgeeks.org/treemap-in-java/)
  * The map is sorted according to the natural ordering of its keys, or by a Comparator provided at map creation time
  *[TreeMap higherKey()](https://www.geeksforgeeks.org/treemap-higherkey-method-in-java-with-examples/)
    * return the least key strictly greater than the given key, or null if there is no such key
* [HashMap getOrDefault(key, defaultValue)](https://www.geeksforgeeks.org/hashmap-getordefaultkey-defaultvalue-method-in-java-with-examples/)
  * get the value mapped with specified key. If no value is mapped with the provided key then the default value is returned.
* [Integer vs. int](https://www.geeksforgeeks.org/difference-between-an-integer-and-int-in-java/)
  * int is a primitive data type while Integer is a Wrapper class.
  * int, being a primitive data type has got less flexibility. We can only store the binary value of an integer in it.
    * **cannot store null**
  * Since Integer is a wrapper class for int data type, it gives us more flexibility in storing, converting and manipulating an int data.
  * Integer is a class and thus it can call various in-built methods defined in the class. Variables of type Integer store references to Integer objects, just as with any other reference (object) type.
