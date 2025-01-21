class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = []
        n = len(operations)
        for i in range(n):
            if operations[i] not in ['C','D','+']:
                stack.append(int(operations[i]))
            elif operations[i] == 'D':
                stack.append(stack[-1] * 2)
            elif operations[i] == 'C':
                stack.pop()
            elif operations[i] == '+':
                stack.append(stack[-1] + stack[-2])
        s = len(stack)
        total_sum = 0
        print(stack)
        for i in range(s):
            total_sum += stack[i]
        
        return total_sum

#Time complexity: O(n)682. Baseball Game
