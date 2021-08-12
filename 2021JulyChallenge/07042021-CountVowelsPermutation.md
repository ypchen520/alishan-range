# Count Vowels Permutation

## Description

* Given an integer n, your task is to count how many strings of length n can be formed under the following rules:
  * Each character is a lower case vowel ('a', 'e', 'i', 'o', 'u')
  * Each vowel 'a' may only be followed by an 'e'.
  * Each vowel 'e' may only be followed by an 'a' or an 'i'.
  * Each vowel 'i' may not be followed by another 'i'.
  * Each vowel 'o' may only be followed by an 'i' or a 'u'.
  * Each vowel 'u' may only be followed by an 'a'.
* Since the answer may be too large, return it modulo 10^9 + 7.

## Solution

### Hint

* Let dp[i][j] be the number of strings of length i that ends with the j-th vowel.
* Deduce the recurrence from the given relations between vowels.

### DP

* bottom-up
* dp[i][j]
  * dp[3][1]
    * length = 3
    * end with 'a'
    * follow the rules:
      * "...e"a: dp[2][2]
      * "...i"a: dp[2][3]
      * "...u"a: dp[2][5]
  * dp[4][1]
    * length = 4
    * end with 'a'
    * follow the rules:
      * "...e"a: dp[3][2]
      * "...i"a: dp[3][3]
      * "...u"a: dp[3][5]
  * dp[i][1] = dp[i-1][2] + dp[i-1][3] + dp[i-1][5]
  * the same goes for dp[i][2], ..., dp[i][5]
* The variable i depends on the input size n
* Modulo has to be applied to any summation
  * e.g.,

  ```Java
  // dp[i][1] = dp[i-1][2] + dp[i-1][3] + dp[i-1][5]
  int temp = (dp[i-1][2] + dp[i-1][3]) % m;
  dp[i][1] = (temp + dp[i-1][5]) % m;
  ```
