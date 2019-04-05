class Solution:
    def plusOne(self, digits: 'List[int]') -> 'List[int]':
        m = 1
        sum = 0
        for i in digits[::-1]:
            sum += i * m
            m *= 10
        return [int(i) for i in str(sum+1)]
