# Distribute Candies

## Description

* Alice has n candies, where the ith candy is of type candyType[i]. Alice noticed that she started to gain weight, so she visited a doctor.
* The doctor advised Alice to only eat n / 2 of the candies she has (n is always even). Alice likes her candies very much, and she wants to eat the maximum number of different types of candies while still following the doctor's advice.
* Given the integer array candyType of length n, return the maximum number of different types of candies she can eat if she only eats n / 2 of them.

## Solution

### Hint

1. To maximize the number of kinds of candies, we should try to distribute candies such that Alice will gain all kinds.
2. What is the upper limit of the number of kinds of candies Alice will gain? Remember candies are to distributed equally.
3. Which data structure is the most suitable for finding the number of kinds of candies?
4. Will hashset solves the problem? Inserting all candies kind in the hashset and then checking its size with upper limit.

### HashMap

* min(Set.size(), candies.length/2)
