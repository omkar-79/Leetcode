class Solution:
    def maxArea(self, height: List[int]) -> int:
        n = len(height)
        l = 0
        r = n - 1
        max_area = 0
        while l < r:
            width = r - l
            h = min(height[l], height[r])
            area = h * width
            max_area = max(area, max_area)

            if height[l] < height[r]:
                l += 1
            else:
                r -= 1
        return max_area
    

#Time complexity: O(n)
