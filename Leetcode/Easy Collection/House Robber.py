class Solution:
    def rob(self, nums: 'List[int]') -> 'int':
        a, b = 0, 0
        for house in nums:
            a, b = house + b if house + b > a else a, a
        return a
