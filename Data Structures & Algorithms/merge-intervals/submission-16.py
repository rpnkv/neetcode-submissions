class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        res = [intervals[0]]

        for i_start, i_end in intervals[1:]:
            if i_start <= res[-1][1]:
                res[-1][1] = max(res[-1][1], i_end)
            else:
                res.append([i_start, i_end])
        return res
