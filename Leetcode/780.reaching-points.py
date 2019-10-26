#
# @lc app=leetcode id=780 lang=python
#
# [780] Reaching Points
#

# @lc code=start


class Solution(object):
    def reachingPoints(self, sx, sy, tx, ty):
        """
        :type sx: int
        :type sy: int
        :type tx: int
        :type ty: int
        :rtype: bool
        """
        if (tx == sx):
            return ty >= sy and (ty-sy) % sx == 0
        if (ty == sy):
            return tx >= sx and (tx-sx) % sy == 0
        stack = [(tx, ty)]
        while stack:
            x, y = stack.pop()
            if x > y and (x - y) >= sx:
                stack.append((x-y, y))
                if x-y == sx:
                    return y >= sy and (y-sy) % sx == 0
                if (x-y, y) == (sx, sy):
                    return True
            if y > x and (y - x) >= sy:
                stack.append((x, y-x))
                if y-x == sy:
                    return x >= sx and (x-sx) % sy == 0
                if (x, y-x) == (sx, sy):
                    return True
        return False

# @lc code=end
