# Max Consecutive Ones III

## Description

* Given a binary array nums and an integer k, return the maximum number of consecutive 1's in the array if you can flip at most k 0's.

## Solution

### Hint

* One thing's for sure, we will only flip a zero if it extends an existing window of 1s. Otherwise, there's no point in doing it, right? Think Sliding Window!
* Since we know this problem can be solved using the sliding window construct, we might as well focus in that direction for hints. Basically, in a given window, we can never have > K zeros, right?
* We don't have a fixed size window in this case. The window size can grow and shrink depending upon the number of zeros we have (we don't actually have to flip the zeros here!).
* The way to shrink or expand a window would be based on the number of zeros that can still be flipped and so on.

### Sliding window

* keep track of the leftmost starting point of the sliding window
* never allow more then k zeroes in the window
