class Solution:
    def trap(self, height: List[int]) -> int:
        left = right = 0
        n = len(height)
        max_l = [0] * n
        max_r = [0] * n

        for i in range(n):
            j = -i-1
            max_l[i] = left
            max_r[j] = right
            left = max(left, height[i])
            right = max(right, height[j])
        #print(max_l)
        #print(max_r)
        total_sum = 0
        for i in range(n):
            capacity= min(max_l[i],max_r[i])
            total_sum += max(0, capacity-height[i])
        return total_sum

#Time complexity: O(n)
