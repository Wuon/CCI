class Solution:
    def rotate(self, nums: 'List[int]', k: 'int') -> 'None':
        if not nums or k <= 0:
            return
        k %= len(nums)
        end = len(nums) - 1
        self.reverse(nums, 0, end - k)
        self.reverse(nums, end - k + 1, end)
        self.reverse(nums, 0, end)

    def reverse(self, nums: 'List[int]', start: 'int', end: 'int') -> 'None':
        if start > end:
            return
        nums[start], nums[end] = nums[end], nums[start]
        self.reverse(nums, start + 1, end - 1)