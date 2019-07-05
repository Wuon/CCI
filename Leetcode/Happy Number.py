class Solution:
    def isHappy(self, n: int) -> bool:
        if n == 1:
            return True
        s = set()
        while n != 1:
            temp = n
            sum = 0
            while temp != 0:
                sum += (temp % 10) ** 2
                temp //= 10
            n = sum
            if n in s:
                return False
            else:
                s.add(n)
            if sum == 1:
                return True
