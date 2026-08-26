class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        lens = [1] * len(nums)

        for start_pos, start_val in enumerate(nums):
            curr_len = lens[start_pos]
            
            for curr_pos in range(start_pos, len(nums)):
                if nums[curr_pos] > start_val:
                    lens[curr_pos] = max(lens[curr_pos], curr_len + 1)
        
        return max(lens)