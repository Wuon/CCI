#
# @lc app=leetcode id=1262 lang=python
#
# [1262] Greatest Sum Divisible by Three
#

# @lc code=start

class Solution:
    def maxSumDivThree(self, nums: List[int]) -> int:
        curSum = 0
        minRemainderTwo = 10001
        minRemainderOne = 10001
        for num in nums:
            curSum += num
            if num % 3 == 2:
                minRemainderOne = min(minRemainderOne, minRemainderTwo + num)
                minRemainderTwo = min(minRemainderTwo, num)
            if num % 3 == 1:
                minRemainderTwo = min(minRemainderTwo, minRemainderOne + num)
                minRemainderOne = min(minRemainderOne, num)
        if curSum % 3 == 0:
            return curSum
        if curSum % 3 == 1 and minRemainderOne != 10001:
            return curSum - minRemainderOne
        if curSum % 3 == 2 and minRemainderTwo != 10001:
            return curSum - minRemainderTwo
        return 0
# @lc code=end
