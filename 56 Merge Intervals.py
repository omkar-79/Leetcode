class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x: x[0])
        merged = []

        for i in range(len(intervals) - 1):
            current = intervals[i]
            next_interval = intervals[i + 1]
            
            if current[1] >= next_interval[0]:
                next_interval[0] = current[0]
                next_interval[1] = max(current[1], next_interval[1])
            else:  
                merged.append(current)
        
        merged.append(intervals[-1])

        return merged

  #Time complexity: O(nlogn)
