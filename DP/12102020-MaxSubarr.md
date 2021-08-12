## Maximum Subarray
* Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.
# Kadane’s Algorithm
* Initialize:
  * max_so_far = 0
  * max_ending_here = 0
* Loop for each element of the array
  * max_ending_here = max_ending_here + a[i]
  * if(max_so_far < max_ending_here)
    * max_so_far = max_ending_here
  * if(max_ending_here < 0)
    * max_ending_here = 0
* return max_so_far
