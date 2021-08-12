# Find Peak Element

## Description

* A peak element is an element that is strictly greater than its neighbors.
* Given an integer array nums, find a peak element, and return its index. If the array contains multiple peaks, return the index to any of the peaks.
* You may imagine that nums[-1] = nums[n] = -∞.
* You must write an algorithm that runs in O(log n) time.
* nums[i] != nums[i + 1] for all valid i.

## Solution

### Binary Search

* distinct neighbors
* 1st scenario
  * mid is a peak: we find our solution
* 2nd scenario
  * right neighbor > mid: there must be a peak on the right side (either one of the elements or the rightmost one)
* 3rd scenario
  * left neighbor > mid: there must be a peak on the left side (either one of the elements or the leftmost one)
* 4th scenario
  * right neighbor > mid and left neighbor > mid
    * we can go either way

### Recursive Binary Search

```Java
public class Solution {
    public int findPeakElement(int[] nums) {
        return search(nums, 0, nums.length - 1);
    }
    public int search(int[] nums, int l, int r) {
        if (l == r)
            return l;
        int mid = (l + r) / 2;
        if (nums[mid] > nums[mid + 1])
            return search(nums, l, mid);
        return search(nums, mid + 1, r);
    }
}
```
