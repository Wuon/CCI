#
# @lc app=leetcode id=394 lang=python
#
# [394] Decode String
#

# @lc code=start
class Solution(object):
    def decodeString(self, s):
        """
        :type s: str
        :rtype: str
        """
        stack = []
        content = ''
        multi = 0
        digits = set(['0','1','2','3','4','5','6','7','8','9'])
        for char in s:
            if char == '[':
                stack.append((content, multi))
                content = ''
                multi = 0
            elif char == ']':
                cur = stack.pop()
                content = cur[0] + cur[1] * content
            elif char in digits:
                multi *= 10
                multi += int(char)
            else:
                content += char
        return content


# @lc code=end
