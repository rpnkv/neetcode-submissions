class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda l: l[0])

        output = intervals[:1]

        for curr in intervals[1:]:
            prev = output[-1]
            if curr[0] <= prev[1]:
                prev[1] = max(curr[1], prev[1])
            else:
                output.append(curr)
        
        return output