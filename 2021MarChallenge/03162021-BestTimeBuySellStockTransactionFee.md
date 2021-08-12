# Best Time to Buy and Sell Stock with Transaction Fee

## Description

* You are given an array prices where prices[i] is the price of a given stock on the ith day, and an integer fee representing a transaction fee.
* Find the maximum profit you can achieve. You may complete as many transactions as you like, but you need to pay the transaction fee for each transaction.
* Note: You may not engage in multiple transactions simultaneously (i.e., you must sell the stock before you buy again).

## Solution

### Hint

* Consider the first K stock prices. At the end, the only legal states are that you don't own a share of stock, or that you do. Calculate the most profit you could have under each of these two cases.

### [Dynamic Programming](https://github.com/cherryljr/LeetCode/blob/master/Best%20Time%20to%20Buy%20and%20Sell%20Stock%20with%20Transaction%20Fee.java)

* For the i<sup>th</sup> day, we have two situations
  * Hold stock
    * do nothing: hold[i-1]
    * buy stock: nothold[i-1] - prices[i]
  * Not holding any stock
    * do nothing: nothold[i-1]
    * sell stock: hold[i-1] + prices[i] - fee

### Java

* [Why is infinity = 0x3f3f3f3f?](https://stackoverflow.com/questions/18429021/why-is-infinity-0x3f3f3f3f)