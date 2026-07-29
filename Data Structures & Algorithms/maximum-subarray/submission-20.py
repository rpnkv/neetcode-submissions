class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        res = -1001

        for i, n in enumerate(nums):
            curr = n
            res = max(curr, res)
            for j in range(i + 1, len(nums)):
                curr += nums[j]
                res = max(curr, res)
        
        return res
