#
# @lc app=leetcode id=1309 lang=python
#
# [1309] Decrypt String from Alphabet to Integer Mapping
#

# @lc code=start

class Solution:
    def freqAlphabets(self, s: str) -> str:
        output = ''
        i = 2
        while i < len(s):
            if s[i] == '#':
                val = int(s[i-2] + s[i-1])
                output += (chr(val + 96))
                i += 2
            else:
                output += (chr(int(s[i - 2]) + 96))
            i += 1
        if i >= len(s):
            for x in range(i - 2, len(s)):
                output += (chr(int(s[x]) + 96))
        return output

# @lc code=end
