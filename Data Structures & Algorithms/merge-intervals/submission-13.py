class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()

        res = [intervals[0]]

        for i, (new_start, new_end) in enumerate(intervals[1:]):
            if new_start <= res[-1][1]:
                res[-1][1] = max(new_end, res[-1][1])
            else:
                res.append(intervals[i + 1])
        
        return res