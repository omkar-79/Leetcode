class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        n = len(tokens)
        stack = []
        for i in range(n):
            if tokens[i] not in '+-/*':
                stack.append(int(tokens[i]))
            else:
                y = stack.pop()
                x = stack.pop()
                if tokens[i] ==  '+':
                    stack.append(x + y)
                elif tokens[i] ==  '-':
                    stack.append(x - y)
                elif tokens[i] ==  '*':
                    stack.append(x * y)
                elif tokens[i] ==  '/':
                    stack.append(int(x / y))
        return stack[0]

#Time complexity: O(n)
