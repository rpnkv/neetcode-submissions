class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = {}

        for i, n in enumerate(nums):
            if n in d:
                d[n].append(i)
            else:
                d[n] = [i]

        for n in nums:
            if target == n * 2:
                if len(d[n]) == 2:
                    return d[n]
                else:
                    continue

            if target - n in d:
                res = [d[n][0], d[target - n][0]]
                res.sort()
                return res
