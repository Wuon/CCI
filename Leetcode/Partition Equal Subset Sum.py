class Solution:
    def canPartition(self, nums: 'List[int]') -> bool:
        total = 0
        for num in nums:
            total += num
        if total % 2 != 0:
            return False
        total /= 2
        total = int(total)
        table = [0 for i in range(total + 1)]
        table[0] = True
        for num in nums:
            for i in range(total, -1, -1):
                if i >= num:
                    table[i] = table[i] or table[i - num]
        return table[total]
