class Solution(object):
    def isValid(self, s):
        stack = []
        for c in s:
            if c == ")":
                if len(stack) == 0 or stack.pop() != "(":
                    return False
            elif c == "}":
                if len(stack) == 0 or stack.pop() != "{":
                    return False
            elif c == "]":
                if len(stack) == 0 or stack.pop() != "[":
                    return False
            else:
                stack.append(c)
        return len(stack) == 0
