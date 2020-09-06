#
# @lc app=leetcode id=9 lang=python3
#
# [9] Palindrome Number
#

# @lc code=start
from collections import deque

class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        q = deque()
        copy = x
        while copy != 0:
            q.append(copy % 10)
            copy = copy // 10
        while len(q) > 1:
            if q.popleft() != q.pop():
                return False
        return True
# @lc code=end
