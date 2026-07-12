class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda i: i[0])

        prev_start, prev_end = intervals[0]
        res = []

        for i, curr_start, curr_end in intervals[1:]:
            if prev_end >= curr_start:
                prev_end = max(prev_end, curr_end)
            else:
                res.append(intervals[i-1])
            
        res.append([prev_start, prev_end])
        
        return res