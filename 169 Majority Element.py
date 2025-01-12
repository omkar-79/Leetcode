class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        freq_dict = {}
        majority = len(nums) // 2
        for n in nums:
            if n not in freq_dict:
                freq_dict[n] = 1
            else:
                freq_dict[n] += 1
            if freq_dict[n] > majority:
                return n
