#
# @lc app=leetcode id=796 lang=python
#
# [796] Rotate String
#

# @lc code=start
class Solution(object):
    def rotateString(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: bool
        """
        if len(A) != len(B):
            return False

        if len(A) == 0:
            return True

        length = len(A)
        search = A[0]

        def check(pos):
            temp = pos
            for i in range(length):
                if i + temp > length - 1:
                    temp = i * -1
                if A[i] != B[i + temp]:
                    return False
            return True

        for pos, letter in enumerate(B):
            if letter == search:
                if check(pos):
                    return True
        return False

# @lc code=end
