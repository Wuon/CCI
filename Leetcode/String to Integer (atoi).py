class Solution:
    def myAtoi(self, str: str) -> int:
        str = str.strip(' ')
        s = []
        start = 0
        if not str or len(str) == 0:
            return 0
        if (not str[0].isdigit()) and str[0] != '-' and str[0] != '+':
            return 0
        if str[0] == '-':
            start = 1
            s.append('-')
        if str[0] == '+':
            start = 1
            s.append('+')
        for i in range(start, len(str)):
            if not str[i].isdigit():
                break
            s.append(str[i])
        if s == ['-'] or s == ['+']:
            return 0
        num = int(''.join(s))
        return num if -2 ** 31 < num < 2 ** 31 else (2 ** 31 if num > 2 ** 31-1 else -2 ** 31)

print(Solution().myAtoi('   +1'))