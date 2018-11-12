# ATTEMPT ONE
# 
# Time Complexity: O(mn)
#
# For any given matrix m*n, during the first iteration,
# we are unable to mutate the matrix otherwise everything
# will be zeros. Instead we store which rows and columns
# are affected and in the second iteration O(2mn) we 
# modify any elements that have a row or column stored
# in the first iteration.

def zeroMatrix(m):
    row = []
    column = []
    for i in range(0,len(m)):
        for j in range(0, len(m[0])):
            if(m[i][j] == 0):
                if i not in row:
                    row.append(i)
                if j not in column:
                    column.append(j)
    for i in range(0,len(m)):
        for j in range(0, len(m[0])):
            if(i in row or j in column):
                m[i][j] = 0

