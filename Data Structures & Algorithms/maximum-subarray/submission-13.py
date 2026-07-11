class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        
        total = sum(nums)
        sum_max = -1001

        for i, n in enumerate(nums):
            curr = n
            sum_max = max(curr, sum_max)
            for j, k in enumerate(nums[i+1:]):
                curr += k
                sum_max = max(curr, sum_max)
            
        return sum_max