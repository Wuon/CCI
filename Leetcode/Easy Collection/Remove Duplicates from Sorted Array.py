class Solution:
    def removeDuplicates(self, nums: 'List[int]') -> 'int':
        end = len(nums)
        start = 1
        while start < end:
            if nums[start] == nums[start-1]:
                nums.pop(start)
                end -= 1
            else:
                start += 1
        return len(nums)
