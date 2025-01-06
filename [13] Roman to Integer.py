class Solution:
    def romanToInt(self, s: str) -> int:
        roman_dict = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        s = list(s)
        total = 0
        prev_value = 0
        for i in reversed(s):
            curr_value = roman_dict[i]
            if curr_value < prev_value:
                total -= curr_value
            else:
                total += curr_value
            prev_value = curr_value
        return total
