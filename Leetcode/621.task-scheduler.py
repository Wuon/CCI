#
# @lc app=leetcode id=621 lang=python
#
# [621] Task Scheduler
#

# @lc code=start
class Solution(object):
    def leastInterval(self, tasks, n):
        """
        :type tasks: List[str]
        :type n: int
        :rtype: int
        """
        store = [0 for i in range(26)]
        for task in tasks:
            store[ord(task) - 65] += 1
        greatest = max(store)
        occurence = store.count(greatest)
        return max(len(tasks), (greatest - 1) * (n + 1) + occurence)


# @lc code=end
