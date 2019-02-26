from collections import Counter

class Solution:
    def intersect(self, nums1: 'List[int]', nums2: 'List[int]') -> 'List[int]':
        ref = Counter(nums2)
        hashset = set(nums2)
        result = []
        for i in nums1:
            if i in hashset:
                if ref[i] != 0:
                    result.append(i)
                    ref[i] -= 1
        return result
