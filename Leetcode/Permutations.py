class Solution:
    def permute(self, nums: 'List[int]') -> 'List[List[int]]':
        o = []
        self.exhaust(nums, 0, len(nums) - 1, o)
        return o

    def exhaust(self, a, l, r, o):
        if l == r:
            o.append(a.copy())
        else:
            for i in range(l, r+1):
                a[l], a[i] = a[i], a[l]
                self.exhaust(a, l+1, r, o)
                a[l], a[i] = a[i], a[l]
