class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram_dict = defaultdict(list)
        for s in strs:
            pat = [0] * 26
            for c in s:
                pat[ord(c)-ord('a')] +=1
            key = tuple(pat)
            anagram_dict[key].append(s)

        return list(anagram_dict.values())

        #Time complexity: O(m*n)
        
