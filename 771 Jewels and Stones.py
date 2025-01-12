class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        jw = set(jewels)
        count = 0
        for i in stones:
            if i in jw:
                count +=1
        return count
