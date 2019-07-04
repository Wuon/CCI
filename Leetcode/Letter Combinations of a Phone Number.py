class Solution:
    def __init__(self):
        self.d = {
            '2': ['a','b','c'],
            '3': ['d','e','f'],
            '4': ['g','h','i'],
            '5': ['j','k','l'],
            '6': ['m','n','o'],
            '7': ['p','q','r','s'],
            '8': ['t','u','v'],
            '9': ['w','x','y','z']
        }

    def letterCombinations(self, digits: str) -> 'List[str]':
        o = []
        self.exhaust(digits, '', o)
        return o

    def exhaust(self, digits, c, o):
        if len(digits) == 0:
            if len(c) != 0:
                o.append(c)
        else:
            digit = digits[0]
            for letter in self.d[digit]:
                self.exhaust(digits[1:], c + letter, o)
