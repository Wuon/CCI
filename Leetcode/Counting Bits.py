class Solution:
    def countBits(self, num: int) -> 'List[int]':
        o = []
        d = [0]
        for i in range(num+1):
            o.append(d.count(1))
            d[0] += 1
            for i in range(len(d)+1):
                if d[i] == 2:
                    d[i] = 0
                    if i+1 == len(d):
                        d.append(1)
                        break
                    else:
                        d[i+1] += 1
                else:
                    break
        return o
