class Solution:
    def repeatedNTimes(self, A: 'List[int]') -> 'int':
        search = len(A) / 2
        d = {}
        for num in A:
            if num not in d:
                d[num] = 1
            else:
                d[num] += 1
            if d[num] == search:
                return num
        return None
