class Solution:
    def maxProfit(self, prices: 'List[int]') -> 'int':
        if not prices:
            return 0
        start = prices[0]
        total = 0
        for i in range(0, len(prices)-1):
            if start < prices[i+1]:
                peak = prices[i+1]
                total += peak - start
                start = peak
            else:
                start = prices[i+1]
        return total
