class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        curr_sum = max_sum = nums[0]

        for n in nums[1:]:
            if curr_sum < 0:
                curr_sum = n
            else:
                curr_sum += n
            
            max_sum = max(curr_sum, max_sum)
        
        return max_sum