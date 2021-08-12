# Max Number of K-Sum Pairs

## Description

* You are given an integer array nums and an integer k.
* In one operation, you can pick two numbers from the array whose sum equals k and remove them from the array.

* Return the maximum number of operations you can perform on the array.

## Solution

### Hint

* The abstract problem asks to count the number of disjoint pairs with a given sum k.
* For each possible value x, it can be paired up with k - x.
* The number of such pairs equals to min(count(x), count(k-x)), unless that x = k / 2, where the number of such pairs will be floor(count(x) / 2).

### Python3

* Counter
  * from collection import Counter
  * DICT = Counter(ARR)
* dict
  * DICT.items()
  * removing element
    * DICT.pop()
    * del
  * get
    * dict.get(key, default = None)
