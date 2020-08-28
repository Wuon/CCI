"""
Given an array with n objects colored red, white or blue, sort them in-place so that objects of the same color are adjacent, with the colors in the order red, white and blue.

Here, we will use the integers 0, 1, and 2 to represent the color red, white, and blue respectively.

Note: You are not suppose to use the library's sort function for this problem.

Example:

Input: [2,0,2,1,1,0]
Output: [0,0,1,1,2,2]
"""

"""
1. 2 index to keep track of 0 and 2
2. iterate and when we fall on:
    0 - move to most left
    1 - skip
    2 - move to most right

[1,0,0,0,0,1]
[2,0,2,1,1,0]

[0,1,0,0,1,0]
[0,0,2,1,1,2]

[0,0,1,0,1,0]
[0,0,2,1,1,2]

[0,0,0,1,0,0]
[0,0,1,1,2,2]

[2,1,2,1,0,0]
[0,1,2,1,0,2]
"""


def sortColors(store):
    l = 0
    curPointer = 0
    r = len(store) - 1
    while curPointer <= r:
        cur = store[curPointer]
        if cur == 0:
            store[curPointer], store[l] = store[l], store[curPointer]
            l += 1
            curPointer += 1
        elif cur == 2:
            store[curPointer], store[r] = store[r], store[curPointer]
            r -= 1
        else:
            curPointer += 1

    return store

print(sortColors([2,0,2,1,1,0]))
print(sortColors([2,0,1]))
