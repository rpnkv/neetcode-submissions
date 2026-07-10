# v4
class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        new_start, new_end = newInterval

        res = []

        for i, (curr_start, curr_end) in enumerate(intervals):
            if curr_end < new_start:
                res.append(intervals[i])
            else:
                break

        for j, (curr_start, curr_end) in enumerate(intervals[i:]):
            if new_end < curr_start:
                break
            else:
                new_start = min(curr_start, new_start)
                new_end = max(curr_end, new_end)
        else:
            j += 1

        res.append([new_start, new_end])
        res += intervals[i + j:]

        return res