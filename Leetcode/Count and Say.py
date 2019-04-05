class Solution:
    def countAndSay(self, n: int) -> str:
        o = '1'
        for i in range(n - 1):
            cur = o[0]
            temp = ''
            count = 0
            for c in o:
                if cur == c:
                    count += 1
                else:
                    temp += str(count) + cur
                    cur = c
                    count = 1
            temp += str(count) + cur
            o = temp
        return o
