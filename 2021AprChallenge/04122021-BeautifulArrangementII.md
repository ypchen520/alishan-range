# Beautiful Arrangement II

## Description

* Given two integers n and k, you need to construct a list which contains n different positive integers ranging from 1 to n and obeys the following requirement:
  * Suppose this list is [a1, a2, a3, ... , an], then the list [|a1 - a2|, |a2 - a3|, |a3 - a4|, ... , |an-1 - an|] has exactly k distinct integers.
* If there are multiple answers, print any of them.

## [Solution](https://twchen.gitbook.io/leetcode/array/beautiful-arrangement-ii)

* place k numbers in an alternating way: [1, n, 2, n-1, 3, n-2, ...], so there are k - 1 distinct absolute differences. Then place the remaining numbers in increasing or decreasing order. That is, the last distinct absolute difference is 1
