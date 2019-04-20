class Solution:
    def flipAndInvertImage(self, A: 'List[List[int]]') -> 'List[List[int]]':
        for i in range(len(A)):
            for j in range(len(A[0])):
                if A[i][j] == 0:
                    A[i][j] = 1
                else:
                    A[i][j] = 0
        for i in range(len(A)):
            for j in range(len(A[0])//2):
                A[i][j], A[i][len(A[0])-j-1] = A[i][len(A[0])-j-1], A[i][j]
        return A
