class Solution:
    def threeSum(self, nums: 'List[int]') -> 'List[List[int]]':
        if len(nums) < 3:
            return []
        if len(set(nums)) == 1 and nums[0] == 0:
            return [[nums[0], nums[0], nums[0]]]
        nums.sort()
        s = set()
        for i in range(len(nums) - 2):
            q = self.twoSum(nums[i + 1:], -nums[i])
            if len(q) != 0:
                for a, b in q:
                    s.add((nums[i], a, b))
        return list(s)

    def twoSum(self, nums: 'List[int]', target: 'int') -> 'List[int]':
        hashmap = {}
        a = []
        for i in range(0, len(nums)):
            if target - nums[i] in hashmap:
                a.append([nums[hashmap[target - nums[i]]], nums[i]])
            hashmap[nums[i]] = i
        return a
