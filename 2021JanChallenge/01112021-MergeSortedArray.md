# Merge Sorted Array

## Description

* Given two sorted integer arrays nums1 and nums2, merge nums2 into nums1 as one sorted array.

* The number of elements initialized in nums1 and nums2 are m and n respectively. You may assume that nums1 has enough space (size that is equal to m + n) to hold additional elements from nums2.

## Solution

```Python
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        l1 = m
        l2 = n
        while l1 > 0 and l2 > 0:
            if nums1[l1-1] > nums2[l2-1]:
                nums1[l1+l2-1] = nums1[l1-1]
                l1 -= 1
            else:
                nums1[l1+l2-1] = nums2[l2-1]
                l2 -= 1
        while l2 > 0:
            nums1[l1+l2-1] = nums2[l2-1]
            l2 -= 1
```
