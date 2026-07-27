class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        removed = 0

        _, prev_end = intervals[0]

        for start, end in intervals[1:]:
            if start < prev_end:
                removed += 1
                prev_end = min(end, prev_end)
            
        return removed
