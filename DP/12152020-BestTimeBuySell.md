## Best Time to Buy and Sell Stock
* Say you have an array for which the ith element is the price of a given stock on day i.
* If you were only permitted to complete at most one transaction (i.e., buy one and sell one share of the stock), design an algorithm to find the maximum profit.

* Note that you cannot sell a stock before you buy one
# Brute Force
# One Pass
* find the largest peak following the smallest valley
* keep track of the **lowest price** and the **largest profit**
