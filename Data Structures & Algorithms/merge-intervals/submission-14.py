class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()

        res = [intervals[0]]


        for i, (curr_start, curr_end) in enumerate(intervals[1:]):
            if res[-1][1] < curr_start:
                res.append(intervals[i + 1])
            else:
                res[-1][1] = max(curr_end, res[-1][1])
        
        return res

