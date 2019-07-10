class Solution:
    def mySqrt(self, x: int) -> int:
        if x <= 1:
            return x
        left = 1
        right = x
        while left <= right:
            mid = left + (right - left) // 2
            sqrt = x // mid
            if sqrt == mid:
                return mid
            elif mid > sqrt:
                right = mid - 1
            else:
                left = mid + 1
        return right
