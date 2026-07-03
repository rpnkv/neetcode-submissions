class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = [1] * len(nums)

        for i in range(len(nums) - 2, -1, -1):
            prefix[i] = nums[i] * prefix[i+1]
        
        suffix = [1] * len(nums)
        for i in range(1, len(nums)):
            suffix[i] = nums[i] * suffix[i-1]
        
        return [a * b for a,b in zip(suffix, prefix)]