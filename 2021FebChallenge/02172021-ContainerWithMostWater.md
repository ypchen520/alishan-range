# Container With Most Water

## Description

* Given n non-negative integers a1, a2, ..., an , where each represents a point at coordinate (i, ai).
* n vertical lines are drawn such that the two endpoints of the line i is at (i, ai) and (i, 0)
* Find two lines, which, together with the x-axis forms a container, such that the container contains the most water.

## Solution

### Hint

* The aim is to maximize the area formed between the vertical lines. The area of any container is calculated using the shorter line as length and the distance between the lines as the width of the rectangle.
  * Area = length of shorter vertical line * distance between lines
* **Start with the maximum width container** and go to a shorter width container if there is a vertical line longer than **the current containers shorter line**. This way we are compromising on the width but we are looking forward to a longer length container.

### Two pointers

* if the value first index is less than the last index increase the first index else decrease the last index
* time complexity: O(n)

