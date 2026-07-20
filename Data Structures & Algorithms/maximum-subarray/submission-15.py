class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_sub = nums[0]

        for i, n  in enumerate(nums):
            curr_sub = None
            for j in range(i, len(nums)):
                if not curr_sub:
                    curr_sub = nums[j]
                else:
                    curr_sub += nums[j]
                
                max_sub = max(max_sub, curr_sub)
        
        return max_sub
