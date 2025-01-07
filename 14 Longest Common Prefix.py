class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        min_len = len(strs[0])
        for s in strs:
            if len(s) < min_len:
                min_len = len(s)
        i = 0
        while i < min_len:
            for s in strs:
                if s[i] != strs[0][i]:
                    return s[:i]
            i += 1
        return strs[0][:i]
