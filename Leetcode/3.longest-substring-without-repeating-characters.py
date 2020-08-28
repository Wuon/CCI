#
# @lc app=leetcode id=3 lang=python3
#
# [3] Longest Substring Without Repeating Characters
#

# @lc code=start
from collections import deque

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        q = deque()
        unique = set()
        largest = 0
        for character in s:
            q.append(character)
            while character in unique:
                unique.remove(q.popleft())
            unique.add(character)
            largest = max(largest, len(q))
        return largest
# @lc code=end
