class Solution:
    def increasingTriplet(self, nums: 'List[int]') -> 'bool':
        if len(nums) < 3:
            return False
        f = s = max(nums) + 1
        for num in nums:
            if num <= f:
                f = num
            elif num <= s:
                s = num
            else:
                return True
        return False
