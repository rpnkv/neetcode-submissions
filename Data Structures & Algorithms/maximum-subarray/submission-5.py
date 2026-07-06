class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_s = min(nums)

        for l, n in enumerate(nums):
            curr_s = n
            max_s = max(curr_s, max_s) 
            for r in range(l+1, len(nums)):
                curr_s += nums[r]
                max_s = max(curr_s, max_s) 
            
        return max_s
