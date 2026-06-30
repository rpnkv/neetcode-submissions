class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        vals = [1] * len(nums)

        for i, num in enumerate(nums):
            for j in range(i, len(nums)):
                if nums[j] > num:
                    vals[j] = vals[i] + 1
                
        
        return max(vals)
