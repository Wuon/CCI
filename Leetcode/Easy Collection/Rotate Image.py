class Solution:
    def rotate(self, matrix: 'List[List[int]]') -> 'None':
        matrix.reverse()
        for i in range(0, len(matrix)):
            for j in range(0, len(matrix[i])):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
