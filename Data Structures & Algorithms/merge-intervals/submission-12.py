class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x: x[0])
        res = []

        res.append(intervals[0])

        for i, (new_start, new_end) in enumerate(intervals[1:]):
            if new_start <= res[-1][1]:
                res[-1][1] = max(res[-1][1], new_end)
            else:
                res.append(intervals[i + 1])
            
        return res