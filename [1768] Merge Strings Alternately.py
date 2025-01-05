class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        merged = []
        length1, length2 = len(word1), len(word2)
        max_length = max(length1, length2)
    
        for i in range(max_length):
            if i < length1:
                merged.append(word1[i])  
            if i < length2:
                merged.append(word2[i])  
                
        return ''.join(merged)
        
