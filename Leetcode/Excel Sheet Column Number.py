class Solution:
    def titleToNumber(self, s: str) -> int:
        multiplier = 0
        row = 0
        for c in s[::-1]:
            row += 26 ** multiplier * (ord(c) - 64)
            multiplier += 1
        return row
