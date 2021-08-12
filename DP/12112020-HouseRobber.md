## House Robber
* adjacent houses have security system connected and it will automatically contact the police if two adjacent houses were broken into on the same night.

* Given a list of non-negative integers representing the amount of money of each house, determine the maximum amount of money you can rob tonight without alerting the police
# DP
* house: keep track of the maximum amount of money **so far**
* nums
* house [i] = max(house[i-2]+nums[i], house[i-1])
# even and odd
# DP with memorization
