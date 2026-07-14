class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = {}

        for i, n in enumerate(nums):
            objective = target - n
            if objective in d:
                return [d[objective], i]
            else:
                d[n] = i
        