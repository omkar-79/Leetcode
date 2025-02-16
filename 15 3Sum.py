class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        n = len(nums)
        final_list = []

        for i in range(n):
            if nums[i] > 0:
                break
            elif i > 0 and nums[i] == nums[i-1]:
                continue
            l = i + 1
            r = n - 1
            while l < r:
                eq = nums[i] + nums[l] + nums[r]
                if eq == 0:
                    final_list.append([nums[i], nums[l], nums[r]])
                    l, r = l + 1, r-1
                    while l < r and nums[l] == nums[l-1]:
                        l += 1
                    while l < r and nums[r] == nums[r+1]:
                        r -= 1
                elif eq < 0:
                    l += 1
                else:
                    r -= 1
        return final_list

        #Time complexity: O(n^2)


        15. 3Sum
