class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda i: i[0])

        prev_start, prev_end = intervals[0]
        removed = 0

        for curr_start, curr_end in intervals[1:]:
            if curr_start < prev_end:
                removed += 1
                prev_end = min(prev_end, curr_end)
            else:
                prev_end = curr_end

        return removed