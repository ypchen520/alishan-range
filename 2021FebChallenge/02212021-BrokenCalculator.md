# Broken Calculator

## Description

* On a broken calculator that has a number showing on its display, we can perform two operations:
  * Double: Multiply the number on the display by 2, or;
  * Decrement: Subtract 1 from the number on the display.
* Initially, the calculator is displaying the number X.
* Return the minimum number of operations needed to display the number Y.

## Solution

### Work Backwards

* while Y > X:
  * Y += 1 (increment) or
  * Y /= 2 (divide)
* if Y == X: X-Y == 0
* if Y < X: X-Y == the number of operation needed (subtraction only)
