# Next Permutation

## Description

* Implement next permutation, which rearranges numbers into the lexicographically next greater permutation of numbers.
* If such an arrangement is not possible, it must rearrange it as the lowest possible order (i.e., sorted in ascending order).
* The replacement must be in place and use only constant extra memory.
* e.g.
  * (2,3,5) < (2,5,3) < (3,2,5) < (3,5,2) < (5,2,3) < (5,3,2)

## Solution

1. start from the right most element
2. find the first element that violates the descending order (index: x)
   * e.g. (2,5,3) -> 2 is the first one from the right that is not in the descending order
3. start from the right most element, find the closest element that are larger than the element found in 2., and then swap them
4. after swapping, the elements after the index "x" should still be in descending order
   * e.g. (2,5,3) -> (3,5,2)
5. reverse the elements after the index "x"

### Python

* reverse list
  * reversed()
    * we neither reverse a list in-place(modify the original list), nor we create any copy of the list
    * we get a reverse iterator
  * reverse()
    * we can reverse the contents of the list object in-place
  * slicing
    * new_lst = lst[::-1]
* reverse a sublist in a list in place
  * lst[start:end+1] = lst[start:end+1][::-1]
