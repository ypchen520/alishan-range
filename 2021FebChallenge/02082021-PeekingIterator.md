# Peeking Iterator

## Description

* Given an Iterator class interface with methods: next() and hasNext(), design and implement a PeekingIterator that support the peek() operation -- it essentially peek() at the element that will be returned by the next call to next().
* Follow up: How would you extend your design to be generic and work with all types, not just integer?

## Solution

### Hint

* Think of "looking ahead". You want to cache the next element.
* Is one variable sufficient? Why or why not?
* Test your design with call order of peek() before next() vs next() before peek().
* For a clean implementation, check out Google's guava library source code.
