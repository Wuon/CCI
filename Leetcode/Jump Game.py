class Solution:
    def canJump(self, nums: List[int]) -> bool:
        reach = nums[0]
        end = len(nums)-1
        if reach >= end:
            return True
        for i in range(1, len(nums)):
            if i > reach:
                return False
            reach = reach if reach > i + nums[i] else i + nums[i]
            if reach >= end:
                return True
        return False
