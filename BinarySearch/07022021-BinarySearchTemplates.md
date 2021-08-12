# Binary Search

## Background

* Search space: a contiguous sequence with a specified left and right index
* maintains the left, right, and middle indices of the search space
* Things to think about
  * how to identify BS problems
  * the reasons for using BS to solve problems

### Three main sections

* Pre-processing: Sort if collection is unsorted.
* Binary Search: Using a loop or **recursion** to divide search space in half after each comparison.
* Post-processing: Determine viable candidates in the remaining space.

### how to identify Binary Search problems

* divides the search space in 2 after every comparison
* every time you need to search for an index or element in a collection.
  * If the collection is unordered, we can always sort it first before applying Binary Search

## Template 1

### Key attributes 1

* Most basic and elementary form of Binary Search
* Search Condition can be determined without comparing to the element's neighbors (or use specific elements around it)
* No post-processing required because at each step, you are checking to see if the element has been found. If you reach the end, then you know the element is not found

### Implementation 1

* int l = 0
* int r = length - 1
* termination: l > r
  * while(l <= r)
* mid = l + (r-l) / 2
* search left: r = mid - 1
* search right: l = mid + 1

### Sqrt(x)

* use int: overflow
  * had to use long
    * cast: return (int) mid;

### Guess number higher or lower

### **Search in rotated sorted array**

* The interesting property of a sorted + rotated array is that when you divide it into two halves, at least one of the two halves will always be sorted

## Template 2

```Java
int binarySearch(int[] nums, int target){
  if(nums == null || nums.length == 0)
    return -1;

  int left = 0, right = nums.length;
  while(left < right){
    // Prevent (left + right) overflow
    int mid = left + (right - left) / 2;
    if(nums[mid] == target){ return mid; }
    else if(nums[mid] < target) { left = mid + 1; }
    else { right = mid; }
  }

  // Post-processing:
  // End Condition: left == right
  if(left != nums.length && nums[left] == target) return left;
  return -1;
}
```

### Key attributes 2

* Search Condition needs to access element's immediate right neighbor
* Use element's right neighbor to determine if condition is met and decide whether to go left or right
* Gurantees Search Space is at least 2 in size at each step
* **Post-processing required**. Loop/Recursion ends when you have 1 element left. Need to assess if the remaining element meets the condition.

### Implementation 2

* int l = 0
* int r = length
* termination: l == r
  * while(l < r)
* mid = l + (r-l) / 2
* search left: r = mid
* search right: l = mid + 1

### First bad version

* return left

## Template 3

```Java
int binarySearch(int[] nums, int target) {
    if (nums == null || nums.length == 0)
        return -1;

    int left = 0, right = nums.length - 1;
    while (left + 1 < right){
        // Prevent (left + right) overflow
        int mid = left + (right - left) / 2;
        if (nums[mid] == target) {
            return mid;
        } else if (nums[mid] < target) {
            left = mid;
        } else {
            right = mid;
        }
    }

    // Post-processing:
    // End Condition: left + 1 == right
    if(nums[left] == target) return left;
    if(nums[right] == target) return right;
    return -1;
}
```

### Key attributes 3

* Search Condition needs to access element's immediate left and right neighbors
* Use element's neighbors to determine if condition is met and decide whether to go left or right
* Gurantees Search Space is at least 3 in size at each step
* Post-processing required.
  * Loop/Recursion ends when you have 2 elements left.
  * Need to assess if the remaining elements meet the condition.

### Implementation 3

* Initial Condition: left = 0, right = length-1
* Termination: left + 1 == right
* Searching Left: right = mid
* Searching Right: left = mid
