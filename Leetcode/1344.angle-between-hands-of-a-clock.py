#
# @lc app=leetcode id=1344 lang=python
#
# [1344] Angle Between Hands of a Clock
#

# @lc code=start

class Solution:
    def angleClock(self, hour: int, minutes: int) -> float:
        minuteAngle = 6 * minutes
        hourAngle = (hour % 12) * 30 + (minutes/60 * 30)
        result = abs(minuteAngle - hourAngle) % 360
        inverse = 360 - result
        return result if result < inverse else inverse

# @lc code=end
