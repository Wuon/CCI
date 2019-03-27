class Solution:
    def maxSubArray(self, nums: 'List[int]') -> 'int':
        if len(nums) == 0:
            return None
        cur, m = 0, nums[0]
        for i in nums:
            cur += i
            if cur > m:
                m = cur
            if cur < 0:
                cur = 0
        return m
