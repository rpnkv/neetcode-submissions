class Solution:
    def rob(self, nums: List[int]) -> int:
        res = [0] * len(nums)

        for i, n in enumerate(nums):
            prev1 = 0 if i < 2 else res[i - 2]
            prev2 = 0 if i < 3 else res[i - 3]
            res[i] = n + max(prev1, prev2)
        
        return max(res[-1:-3:-1])
