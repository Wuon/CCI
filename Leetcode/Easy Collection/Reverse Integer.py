class Solution:
    def reverse(self, x: 'int') -> 'int':
        c = list(str(x))
        if c[0] == '-':
            c.pop(0)
            c.append('-')
        c.reverse()
        o = int(''.join(str(i) for i in c))
        return o if 2 ** 31 * - 1 <= o <= 2 ** 31 - 1 else 0
