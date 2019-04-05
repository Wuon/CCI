class Solution:
    def romanToInt(self, s: 'str') -> 'int':
        sum = 0
        last = ""
        for c in s:
            if c == "M":
                if last == "C":
                    sum += 800
                else:
                    sum += 1000
            elif c == "D":
                if last == "C":
                    sum += 300
                else:
                    sum += 500
            elif c == "C":
                if last == "X":
                    sum += 80
                else:
                    sum += 100
            elif c == "L":
                if last == "X":
                    sum += 30
                else:
                    sum += 50
            elif c == "X":
                if last == "I":
                    sum += 8
                else:
                    sum += 10
            elif c == "V":
                if last == "I":
                    sum += 3
                else:
                    sum += 5
            else:
                sum += 1
            last = c
        return sum
