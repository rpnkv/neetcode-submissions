class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res = []

        new_start, new_end = newInterval

        for i in range(len(intervals)):
            curr_start, curr_end = intervals[i]

            if curr_end < new_start:
                res.append(intervals[i])
            else:
                break

        while i < len(intervals) and new_end > intervals[i][0]:
            new_start = min(intervals[i][0], new_start)
            new_end = max(intervals[i][1], new_end)

            i += 1

        res.append([new_start, new_end])
        res += intervals[i:]

        return res