class Solution:
    def missingNumber(self, nums: 'List[int]') -> 'int':
        s = set(nums)
        for i in range(len(nums)):
            if i not in s:
                return i
        return len(nums)
