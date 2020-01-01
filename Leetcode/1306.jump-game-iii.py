#
# @lc app=leetcode id=1306 lang=python
#
# [1306] Jump Game III
#

# @lc code=start

class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        stack = [start]
        visited = [False for i in range(len(arr))]
        while stack:
            cur = stack.pop()
            if 0 <= cur < len(arr) and visited[cur] == False:
                if arr[cur] == 0:
                    return True
                visited[cur] = True
                stack.append(cur + arr[cur])
                stack.append(cur - arr[cur])
        return False

# @lc code=end
