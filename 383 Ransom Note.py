class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        dict = {}

        for i in magazine:
            if i not in dict:
                dict[i] = 1
            else:
                dict[i] += 1

        for j in ransomNote:
            if j not in dict or dict[j] == 0:
                return False
            else:
                dict[j] -= 1
        return True 
        
