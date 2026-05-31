class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda lst: lst[0])

        res = intervals[:1]

        for intr in intervals[1:]:
            if intr[0] > res[-1][1]:
                res.append(intr)
            else:
                res[-1][1] = max(intr[1], res[-1][1])
            
        return res