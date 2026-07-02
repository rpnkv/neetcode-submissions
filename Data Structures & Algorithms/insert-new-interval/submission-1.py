class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res = []

        new_start, new_end = newInterval

        for start, end in intervals:
            if new_start < end and start < new_end:
                new_start = min(start, new_start)
                new_end = max(end, new_end)
                continue
            else:
                res.append([start, end])

        res.append([new_start, new_end])

        res.sort(key=lambda i: i[0])

        return res