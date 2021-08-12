# Binary Watch

## Description

* A binary watch has 4 LEDs on the top which represent the hours (0-11), and the 6 LEDs on the bottom represent the minutes (0-59).
* Each LED represents a zero or one, with the least significant bit on the right.
* Given a non-negative integer n which represents the number of LEDs that are currently on, return all possible times the watch could represent.

## Solution

### Hint

* Simplify by seeking for solutions that involve comparing bit counts.
* Consider calculating all possible times for comparison purposes.

### Backtracking

### Bit Manipulation

* https://stackoverflow.com/questions/50197416/binary-watch-leetcode
* Using two for loops and 
* only selecting the hour h and minute m for which the sum of set bits is equal to n

### Python

* bit count
  * bin(n).count("1") 
* f-string zero padding
  * f'{h}:{m:02}'
