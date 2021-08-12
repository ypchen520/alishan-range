# Validate Stack Sequences

## Description

* Given two sequences pushed and popped with distinct values, return true if and only if this could have been the result of a sequence of push and pop operations on an initially empty stack.

## Solution

### Simulation

* Push element from |pushed sequence| onto stack s one by one and pop when top of the stack s is equal the current element in the |popped sequence|.
