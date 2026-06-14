class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda i: i[0])

        prev_end = intervals[0][1]
        removed = 0

        for curr_start, curr_end in intervals[1:]:
            if prev_end > curr_start:
                removed += 1
                prev_end = min(curr_end, prev_end)
            else:
                prev_end = curr_end
        
        return removed
