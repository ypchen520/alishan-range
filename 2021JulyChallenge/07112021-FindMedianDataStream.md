# Find Median from Data Stream

## Description

* The median is the middle value in an ordered integer list. If the size of the list is even, there is no middle value and the median is the mean of the two middle values.
  * For example, for arr = [2,3,4], the median is 3.
  * For example, for arr = [2,3], the median is (2 + 3) / 2 = 2.5.
* Implement the MedianFinder class:
  * MedianFinder() initializes the MedianFinder object.
  * void addNum(int num) adds the integer num from the data stream to the data structure.
  * double findMedian() returns the median of all elements so far. Answers within 10-5 of the actual answer will be accepted.

## Solution

### Priority queues

* Max heap: smaller half of the numbers
* Min heap: larger half of the numbers
* findMedian: O(1)
* addNum: O(log n)

### Java

* Priority queue
  * size()
  * add()
  * peek()
  * poll()
