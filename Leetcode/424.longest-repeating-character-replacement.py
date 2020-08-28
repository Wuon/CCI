#
# @lc app=leetcode id=424 lang=python
#
# [424] Longest Repeating Character Replacement
#

# @lc code=start
from collections import deque

class Solution(object):
    def characterReplacement(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        if len(s) == 0:
            return 0
        if k == len(s):
            return k
        count = [0 for i in range(26)]
        front = 0
        record = 0
        for back in range(len(s)):
            count[ord(s[back]) - 65] += 1
            record = max(record, count[ord(s[back]) - 65])
            if record + k <= back - front:
                count[ord(s[front]) - 65] -= 1
                front += 1
        return len(s) - front

    # Solution using queue
    def characterReplacement2(self, s: str, k: int) -> int:
        d = {}
        q = deque()
        largest = 0
        for character in s:
            q.append(character)
            if character not in d:
                d[character] = 0
            d[character] += 1
            shouldChange = len(q) - max(d.values())
            while shouldChange > k:
                d[q.popleft()] -= 1
                shouldChange = len(q) - max(d.values())
            largest = max(len(q), largest)
        return largest

# @lc code=end
