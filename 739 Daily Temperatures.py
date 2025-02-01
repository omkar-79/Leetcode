class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        final_output = [0] * n
        stack = []

        for i, temp in enumerate(temperatures):
            while stack and stack[-1][0] < temp:
                stack_temp, stack_i = stack.pop()
                final_output[stack_i] = i - stack_i
            stack.append((temp, i))
        return final_output

#Time complexity: O(n)
