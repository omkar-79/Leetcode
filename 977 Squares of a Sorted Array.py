class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        l = 0
        r = len(nums) - 1
        final_array = []

        while l <= r:
            if abs(nums[l]) > abs(nums[r]):
                final_array.append(nums[l] ** 2)
                l +=1
            else:
                final_array.append(nums[r] ** 2)
                r -=1
        final_array = final_array[::-1]

        return final_array

        #Time complexity: O(n)
