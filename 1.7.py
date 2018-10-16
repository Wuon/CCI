# ATTEMPT ONE
# 
# Time Complexity: O(n^2)
#
# Expected output from one rotation of 90 degrees
#
#     [0,1,2,3]   =>   [12,8,4,0]
#     [4,5,6,7]   =>   [13,9,5,1]
#   [8,9,10,11]   =>   [14,10,6,2]
# [12,13,14,15]   =>   [15,11,7,3]
#
# For any given matrix n*n, to rotate 90 degrees, we must touch 
# all the points which would produce n^2 time. My algorithm takes
# advantage of the matrix being n*n, because of a squares nature, 
# it becomes easy to manipulate data. Comparing one rotation with 
# another shows that all that is happening is the j index becomes
# the i index and the i index becomes the j index. This follows the
# physical attributes of a 90 degree rotation.

def rotateMatrix(p):
    nP = [[None for i in range(len(p))] for i in range(len(p))]
    for i in range(0, len(p)):
        for j in range(len(p)-1, -1,-1):
            nP[i][len(p)-j-1] = p[j][i]
    return nP