class Solution:
    def singleNumber(self, nums: 'List[int]') -> 'int':
        s = set()
        for i in nums:
            if i in s:
                s.remove(i)
            else:
                s.add(i)
        return s.pop()
