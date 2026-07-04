class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        intervals.sort()
        res = []

        i = 0

        new_start, new_end = newInterval

        while i < len(intervals):
            curr_start, curr_end = intervals[i]
            if intervals[i][1] < new_start: # if current ends before inserting start
                res.append(intervals[i])
                i+=1
            else:
                break

        while i < len(intervals):
            curr_start, curr_end = intervals[i]
            if curr_start <= new_end:
                new_start = min(curr_start, new_start)
                new_end = max(curr_end, new_end)
                i+=1
            else:
                break

        res.append([new_start, new_end])

        res.extend(intervals[i:])

        return res

