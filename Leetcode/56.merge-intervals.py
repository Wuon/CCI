#
# @lc app=leetcode id=56 lang=python
#
# [56] Merge Intervals
#

# @lc code=start
class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        output = []
        intervals.sort()
        for interval in intervals:
            if not output:
                output.append(interval)
            elif interval[0] <= output[-1][1]:
                if interval[1] >= output[-1][1]:
                    output[-1][1] = interval[1]
            else:
                output.append(interval)
        return output


# @lc code=end
