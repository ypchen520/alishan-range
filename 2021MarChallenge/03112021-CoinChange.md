# Coin Change

## Description

* You are given coins of different denominations and a total amount of money amount. Write a function to compute the fewest number of coins that you need to make up that amount. If that amount of money cannot be made up by any combination of the coins, return -1.
* You may assume that you have an infinite number of each kind of coin.

## Solution

### Dynamic Programming (Top down)

### Dynamic Programming (Bottom up)

* constructing a temporary array table[][] in a bottom-up manner
* each element of the 2D array (table[i][j]) tells us the minimum number of coins required to get the sum j, considering the first i coins only
