class Solution:
    def maxProfit(self, prices: 'List[int]') -> 'int':
        if prices == [] or len(prices) == 1:
            return 0
        low, net = prices[0], 0
        for i in range(1, len(prices)):
            if prices[i] < low:
                low = prices[i]
            else:
                change = prices[i] - low
                if change > net:
                    net = change
        return net
