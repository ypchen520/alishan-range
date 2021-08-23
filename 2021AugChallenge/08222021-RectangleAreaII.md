# Rectangle Area II

## Description

* We are given a list of (axis-aligned) rectangles. Each rectangle[i] = [xi1, yi1, xi2, yi2] , where (xi1, yi1) are the coordinates of the bottom-left corner, and (xi2, yi2) are the coordinates of the top-right corner of the ith rectangle.
* Find the total area covered by all rectangles in the plane. Since the answer may be too large, return it modulo 109 + 7.

## Solution

### [Discretization](https://leetcode.com/problems/rectangle-area-ii/discuss/137914/JavaC%2B%2BPython-Discretization-and-O(NlogN))

* Scan from y (i.e., y<sub>0</sub>), keep track of the current **coverage** of x
  * when we scan the next y (i.e., y<sub>1</sub>), add [(i.e., y<sub>1</sub>) - (i.e., y<sub>0</sub>)] * coverage<sub>0</sub> to the cumulative **area**

### Java

#### [TreeSet vs. HashSet](https://www.geeksforgeeks.org/hashset-vs-treeset-in-java/)

* Ordering
  * Elements in HashSet are not ordered. TreeSet maintains objects in Sorted order defined by either Comparable or Comparator method in Java. TreeSet elements are sorted in ascending order by default. It offers several methods to deal with the ordered set like first(), last(), headSet(), tailSet(), etc.

#### [IntStream.range()](https://www.geeksforgeeks.org/intstream-range-java/)

* IntStream range(int startInclusive, int endExclusive) returns a sequential ordered IntStream from startInclusive (inclusive) to endExclusive (exclusive) by an incremental step of 1.
