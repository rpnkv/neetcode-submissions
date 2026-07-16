class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_sum = max(nums)

        for i, n in enumerate(nums):
            curr_sum = n
            for k in range(i+1, len(nums)):
                curr_sum += nums[k]
                max_sum = max(max_sum, curr_sum)

        return max_sum