class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        col = set(nums)
        length = 0
        longest = 0
        for num in col:
            if (num - 1) not in col:
                next_num = num + 1
                length = 1
                while next_num in col:
                    length +=1 
                    next_num +=1 
                longest = max(longest, length)
        return longest

        #Time complexity: O(n)
