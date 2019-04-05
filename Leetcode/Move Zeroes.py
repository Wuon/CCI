class Solution:
    def moveZeroes(self, nums: 'List[int]') -> 'None':
        zero = 0
        for i in range(len(nums)-1, -1, -1):
            if nums[i] == 0:
                nums.pop(i)
                zero += 1
        for i in range(0, zero):
            nums.append(0)
