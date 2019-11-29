#
# @lc app=leetcode id=417 lang=python
#
# [417] Pacific Atlantic Water Flow
#

# @lc code=start

class Solution(object):
    def pacificAtlantic(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[List[int]]
        """
        output = []
        if not matrix:
            return output
        aGrid = [[0 for i in range(len(matrix[0]))] for j in range(len(matrix))]
        bGrid = [[0 for i in range(len(matrix[0]))] for j in range(len(matrix))]
        visited = [[False for i in range(len(matrix[0]))] for j in range(len(matrix))]
        stack = []
        for j in range(len(matrix[0])):
            stack.append([0, j])
        for i in range(1, len(matrix)):
            stack.append([i, 0])
        while stack:
            cur = stack.pop()
            if not visited[cur[0]][cur[1]]:
                visited[cur[0]][cur[1]] = True
                aGrid[cur[0]][cur[1]] = "X"
                if cur[0] + 1 < len(matrix) and matrix[cur[0]][cur[1]] <= matrix[cur[0] + 1][cur[1]]:
                    stack.append([cur[0] + 1, cur[1]])
                if cur[1] + 1 < len(matrix[0]) and matrix[cur[0]][cur[1]] <= matrix[cur[0]][cur[1] + 1]:
                    stack.append([cur[0], cur[1] + 1])
                if cur[0] - 1 >= 0 and matrix[cur[0]][cur[1]] <= matrix[cur[0] - 1][cur[1]]:
                    stack.append([cur[0] - 1, cur[1]])
                if cur[1] - 1 >= 0 and matrix[cur[0]][cur[1]] <= matrix[cur[0]][cur[1] - 1]:
                    stack.append([cur[0], cur[1] - 1])
        visited = [[False for i in range(len(matrix[0]))] for j in range(len(matrix))]
        for j in range(len(matrix[0])):
            stack.append([len(matrix) - 1, j])
        for i in range(0, len(matrix) - 1):
            stack.append([i, len(matrix[0]) - 1])
        while stack:
            cur = stack.pop()
            if not visited[cur[0]][cur[1]]:
                visited[cur[0]][cur[1]] = True
                if (aGrid[cur[0]][cur[1]] == "X"):
                    output.append([cur[0], cur[1]])
                bGrid[cur[0]][cur[1]] = "Y"
                if cur[0] + 1 < len(matrix) and matrix[cur[0]][cur[1]] <= matrix[cur[0] + 1][cur[1]]:
                    stack.append([cur[0] + 1, cur[1]])
                if cur[1] + 1 < len(matrix[0]) and matrix[cur[0]][cur[1]] <= matrix[cur[0]][cur[1] + 1]:
                    stack.append([cur[0], cur[1] + 1])
                if cur[0] - 1 >= 0 and matrix[cur[0]][cur[1]] <= matrix[cur[0] - 1][cur[1]]:
                    stack.append([cur[0] - 1, cur[1]])
                if cur[1] - 1 >= 0 and matrix[cur[0]][cur[1]] <= matrix[cur[0]][cur[1] - 1]:
                    stack.append([cur[0], cur[1] - 1])
        return output

# @lc code=end
