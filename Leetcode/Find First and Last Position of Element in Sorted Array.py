class Solution:
    def searchRange(self, nums: 'List[int]', target: int) -> 'List[int]':
        if not nums:
            return [-1, -1]
        l, r = 0, len(nums) - 1
        while l < r:
            mid = (l + r) // 2
            if nums[mid] > target:
                r = mid
            elif nums[mid] == target:
                r = mid
                l = mid
                break
            else:
                l = mid + 1
        if l == len(nums) or nums[l] != target:
            return [-1, -1]
        while r + 1 < len(nums) and nums[r + 1] == target:
            r += 1
        while l - 1 >= 0 and nums[l - 1] == target:
            l -= 1
        return [l,r]
