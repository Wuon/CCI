#
# @lc app=leetcode id=207 lang=python
#
# [207] Course Schedule
#

# @lc code=start
class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        d = {}
        for prerequisite in prerequisites:
            stack = [prerequisite[0]]
            while stack:
                cur = stack.pop()
                if cur in d:
                    if prerequisite[1] in d[cur]:
                        return False
                    for edge in d[cur]:
                        stack.append(edge)
            if prerequisite[1] in d:
                d[prerequisite[1]].add(prerequisite[0])
            else:
                d[prerequisite[1]] = set([prerequisite[0]])
        return True

# @lc code=end
