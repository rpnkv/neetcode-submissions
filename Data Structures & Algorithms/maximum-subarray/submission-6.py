class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        s_max = s_curr = sum(nums)

        l, r = 0, len(nums) - 1

        while l < r:
            if nums[l] < nums[r]:
                s_curr -= nums[l]
                l += 1
            else:
                s_curr -= nums[r]
                r -= 1
            
            s_max = max(s_max, s_curr)
        
        return s_max