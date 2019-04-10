class Solution:
    def removeOuterParentheses(self, s: 'str') -> 'str':
        stack = []
        new = ""
        for char in s:
            if char == ")":
                stack.pop()
            if len(stack) != 0:
                new += char
            if char == "(":
                stack.append(char)
        return new
