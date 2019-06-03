class Solution:
    def longestMountain(self, A: 'List[int]') -> int:
        max = 0
        a = 0
        b = 0
        descent = False
        for num in A[1:]:
            if num > A[b] and descent == False:
                b += 1
            elif b != a and num < A[b]:
                b += 1
                descent = True
            else:
                if descent:
                    max = b-a+1 if b-a+1 > max else max
                    descent = False
                    a = b
                    b += 1
                    if A[a] == A[b]:
                        a += 1
                else:
                    b += 1
                    a = b
        if descent:
            max = b-a+1 if b-a+1 > max else max
            descent = False
        return max
