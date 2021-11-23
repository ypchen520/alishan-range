# N-th Tribonacci Number

## Description

* The Tribonacci sequence Tn is defined as follows: 
* T0 = 0, T1 = 1, T2 = 1, and Tn+3 = Tn + Tn+1 + Tn+2 for n >= 0.
* Given n, return the value of Tn.

## Solution

### Hint

* Make an array F of length 38, and set F[0] = 0, F[1] = F[2] = 1.
* Now write a loop where you set F[n+3] = F[n] + F[n+1] + F[n+2], and return F[n].
