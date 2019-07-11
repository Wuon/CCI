class Solution:
    def sortColors(self, nums: 'List[int]') -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        zero = -1
        one = 0
        two = len(nums)
        while one < two:
            if nums[one] == 0:
                zero += 1
                nums[zero], nums[one] = nums[one], nums[zero]
                one += 1
            elif nums[one] == 2:
                two -= 1
                nums[two], nums[one] = nums[one], nums[two]
            else:
                one += 1
