class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        dict = {}
        st = 'balloon'
        count = 0
        b =True

        for i in text:
            if i in st:
                dict[i] = dict.get(i, 0) + 1
        while b:
            for s in st:
                if s not in dict or dict[s] == 0:
                    b = False
                    break
                else:
                    dict[s] -=1
            if b:
                count += 1
        return count
        
