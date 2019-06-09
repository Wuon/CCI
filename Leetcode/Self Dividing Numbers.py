class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> 'List[int]':
        o = []
        for i in range(left, right+1):
            cur = i
            c = True
            while cur != 0:
                if cur % 10 != 0:
                    if i % (cur % 10) != 0:
                        c = False
                        break
                else:
                    c = False
                    break
                cur //= 10
            if c:
                o.append(i)
        return o
