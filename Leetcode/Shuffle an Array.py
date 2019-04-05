import random


class Solution:

    def __init__(self, nums: 'List[int]'):
        self.og = nums
        
    def reset(self) -> 'List[int]':
        return self.og

    def shuffle(self) -> 'List[int]':
        cc = self.og[:]
        for i in range(len(cc)):
            j = random.randint(0, len(cc) - 1)
            cc[i], cc[j] = cc[j], cc[i]
        return cc
