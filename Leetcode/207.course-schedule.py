#
# @lc app=leetcode id=207 lang=python
#
# [207] Course Schedule
#

# @lc code=start

from collections import defaultdict, deque
class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        graph = defaultdict(list)
        inbound = defaultdict(int)
        q = deque()
        counter = 0

        for x, y in prerequisites:
            graph[x].append(y)
            inbound[y] += 1

        for i in range(numCourses):
            if inbound[i] == 0:
                q.append(i)

        while q:
            cur = q.popleft()
            for neighbour in graph[cur]:
                inbound[neighbour] -= 1
                if inbound[neighbour] == 0:
                    q.append(neighbour)
            counter += 1

        return counter == numCourses

# @lc code=end
