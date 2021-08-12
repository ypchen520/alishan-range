# A Better Repeated Deletion Algorithm - Intro

* the result Array is smaller than the input Array
* Given a sorted array, remove the duplicates such that each element appears only once
  * O(N<sup>2</sup>)

    ```Java
    class Solution {
        public int removeDuplicates(int[] nums) {
            
            // The initial length is simply the capacity.
            int length = nums.length;
            
            // Assume the last element is always unique.
            // Then for each element, delete it iff it is
            // the same as the one after it. Use our deletion
            // algorithm for deleting from any index.
            for (int i = length - 2; i >= 0; i--) {
                if (nums[i] == nums[i + 1]) {
                    // Delete the element at index i, using our standard
                    // deletion algorithm we learned.
                    for (int j = i + 1; j < length; j++) {
                        nums[j - 1] = nums[j];
                    }
                    // Reduce the length by 1.
                    length--;
                }
            }
            // Return the new length.
            return length;
        }
    }
    ```

  * O(N)
    * do an initial pass, counting the number of unique elements.
    * create the result Array and do a second pass to add the elements into it.
    * space complexity is not O(1)

## Remove Duplicates from Sorted Array

### Description

* Given an integer array nums sorted in non-decreasing order, remove the duplicates in-place such that each unique element appears only once. The relative order of the elements should be kept the same.
* Since it is impossible to change the length of the array in some languages, you must instead have the result be placed in the first part of the array nums. More formally, if there are k elements after removing the duplicates, then the first k elements of nums should hold the final result. It does not matter what you leave beyond the first k elements.
* Return k after placing the final result in the first k slots of nums.
* Do not allocate extra space for another array. You must do this by modifying the input array in-place with O(1) extra memory.

### Solution

* keep track of the number of duplicates
* keep track of the last value
* replace nums[i-numberOfDuplicates] with nums[i] when nums[i] is different from the last value
* return n - numberOfDuplicates

## A Better Repeated Deletion Algorithm - Answer

* it doesn't need to firstly determine the size of the output

### **two-pointer technique**

* We iterate over the array in two different places at the same time
* It is impossible for writePointer to ever get ahead of the readPointer. 
  * This means that we would never overwrite a value that we haven't yet read

### When to Use In-Place Array Operations

* If we'll need the original array values again later, then we shouldn't be overwriting them. In these cases, it's best to create a copy to work with, or to simply not use in-place techniques
* It reduces the space complexity of an algorithm
  * Instead of requiring O(N) space, we can reduce it down to O(1)
