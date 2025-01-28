class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        n = len(s)
        for i in range(n):
            if s[i] == '(' or s[i] == '[' or s[i] == '{':
                stack.append(s[i])
            elif s[i] == ')' and stack and stack[-1] == '(':
                stack.pop()
            elif s[i] == ']' and stack and stack[-1] == '[':
                stack.pop()
            elif s[i] == '}' and stack and stack[-1] == '{':
                stack.pop()
            else:
                return False

        return len(stack) == 0

#Time complexity: O(n)
