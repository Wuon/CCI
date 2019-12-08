#
# @lc app=leetcode id=17 lang=python
#
# [17] Letter Combinations of a Phone Number
#

# @lc code=start
class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        output = []
        if not digits:
            return output
        d = {
            "2": ["a", "b", "c"],
            "3": ["d", "e", "f"],
            "4": ["g", "h", "i"],
            "5": ["j", "k", "l"],
            "6": ["m", "n", "o"],
            "7": ["p", "q", "r", "s"],
            "8": ["t", "u", "v"],
            "9": ["w", "x", "y", "z"],
        }
        stack = [["", list(digits)]]
        while stack:
            cur = stack.pop()
            if not cur[1]:
                output.append(cur[0])
            else:
                for letter in d[cur[1][0]]:
                    stack.append([cur[0] + letter, cur[1][1:]])
        return output



# @lc code=end
