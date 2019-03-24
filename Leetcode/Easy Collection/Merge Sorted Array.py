# TODO Optimize
class Solution:
    def merge(self, nums1: 'List[int]', m: 'int', nums2: 'List[int]', n: 'int') -> None:
        cap = 0
        for i in range(n):
            for j in range(m + n):
                if nums2[i] < nums1[j] or j >= m + cap:
                    self.helper(nums1, j, nums2[i])
                    cap += 1
                    break

    def helper(self, nums1, init, val):
        temp = val
        for i in range(init, len(nums1)):
            nums1[i], temp = temp, nums1[i]
