class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        max_seqs = [1] * len(nums)

        for i, num in enumerate(nums):
            for j in range(i, len(nums)):

                curr_max = max_seqs[i]

                if num < nums[j]:
                    max_seqs[j] = max(max_seqs[j], curr_max + 1)
                
        return max(max_seqs)