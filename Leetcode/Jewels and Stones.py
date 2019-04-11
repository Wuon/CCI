class Solution:
    def numJewelsInStones(self, J: 'str', S: 'str') -> int:
        s = set(J)
        j = 0
        for stone in S:
            if stone in s:
                j += 1
        return j
