class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda l: l[0])

        res = [intervals[0]]

        for i in intervals[1:]:
            prev_start, prev_end = res[-1]
            curr_start, curr_end = i

            if curr_start <= prev_end:
                res[-1][1] = max(curr_end, prev_end)
            else:
                res.append(i)

        return res