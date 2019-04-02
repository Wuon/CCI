class Solution:
    def generate(self, numRows: 'int') -> 'List[List[int]]':
        o = [[1], [1,1]]
        if numRows == 0:
            return []
        if numRows == 1:
            return [[1]]
        if numRows == 2:
            return o
        for i in range (1, numRows - 1):
            x = [1]
            for j in range(i):
                x.append(o[i][j] + o[i][j+1])
            x.append(1)
            o.append(x)
        return o
