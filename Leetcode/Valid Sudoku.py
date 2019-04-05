class Solution:
    def isValidSudoku(self, board: 'List[List[str]]') -> 'bool':
        for i in range(0, 9):
            s1, s2, s3 = set(), set(), set()
            for j in range(0, 9):
                if board[i][j] != '.':
                    if board[i][j] in s1:
                        return False
                    s1.add(board[i][j])
                if board[j][i] != '.':
                    if board[j][i] in s2:
                        return False
                    s2.add(board[j][i])
                if board[(j % 3) + ((3 * i) // 9) * 3][(j // 3) + (3 * i) % 9] != '.':
                    if board[(j % 3) + ((3 * i) // 9) * 3][(j // 3) + (3 * i) % 9] in s3:
                        return False
                    s3.add(board[(j % 3) + ((3 * i) // 9) * 3][(j // 3) + (3 * i) % 9])
        return True
