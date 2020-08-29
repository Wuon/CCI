#
# @lc app=leetcode id=838 lang=python3
#
# [838] Push Dominoes
#

# @lc code=start
class Solution:
    def pushDominoes(self, dominoes: str) -> str:
        lastRight = -1
        lastLeft = 0
        result = list(dominoes)
        for index, character in enumerate(result):
            if character == '.':
                continue
            elif character == 'L':
                if index > lastRight:
                    if lastRight == -1:
                        for j in range(lastLeft, index):
                            result[j] = 'L'
                    else:
                        low = lastRight + 1
                        high = index - 1
                        while low < high:
                            result[low] = 'R'
                            result[high] = 'L'
                            low += 1
                            high -= 1
                lastRight = -1
                lastLeft = index
            else:
                if lastRight != -1:
                    for i in range(lastRight, index):
                        result[i] = 'R'
                lastRight = index
        if lastRight >= lastLeft:
            for i in range(lastRight, len(dominoes)):
                result[i] = 'R'
        return ''.join(result)

# @lc code=end
