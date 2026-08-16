class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        subseqs = [1] * len(nums)

        for i, n in enumerate(nums):
            curr_len = subseqs[i]
            for j in range(i, len(nums)):
                if nums[j] > n:
                    subseqs[j] = max(subseqs[j], curr_len + 1)
            
        return max(subseqs)