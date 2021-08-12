# Boats to Save People

## Description

* The i-th person has weight people[i], and each boat can carry a maximum weight of limit
* Each boat carries **at most 2 people** at the same time, provided the sum of the weight of those people is at most limit.
* Return the minimum number of boats to carry every given person.  (It is guaranteed each person can be carried by a boat.)

## Solution

### Two pointer

* If the heaviest person can share a boat with the lightest person, then do so. 
* Otherwise, the heaviest person can’t pair with anyone, so they get their own boat.
* sort the array
* maintain a pointer for the lightest person and a pointer for the heaviest person

### JAVA

* Arrays
  * Arrays.sort()
  * .length
