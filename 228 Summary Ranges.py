class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        final_list = []
        i = 0
        while i < len(nums):
            start = nums[i]
            while i < len(nums) -1 and nums[i] + 1 == nums[i+1]:
                i+=1
            if start != nums[i]:
                final_list.append(str(start) + '->' + str(nums[i]))
            else:
                final_list.append(str(start))
            i += 1
        return final_list
