class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_sum = min(nums)
        
        for i, n in enumerate(nums):
            curr_sum = n
            for j in range(i + 1, len(nums)):
                curr_sum += nums[j]
                max_sum = max(curr_sum, max_sum)
        
        return max_sum