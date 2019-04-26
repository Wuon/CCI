class Solution:
    def judgeCircle(self, moves: 'str') -> 'bool':
        left = 0
        right = 0
        up = 0
        down = 0
        for char in moves:
            if char == "L":
                left += 1
            elif char == "R":
                right += 1
            elif char == "U":
                up += 1
            else:
                down += 1
        return up == down and right == left
