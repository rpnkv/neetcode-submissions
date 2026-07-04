class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        max_subseqs = [1] * len(nums)

        for i, n in enumerate(nums):
            for j in range(i + 1, len(nums)):
                if nums[j] > n:
                    max_subseqs[j] = max(max_subseqs[j], max_subseqs[i] + 1)
        

        return max(max_subseqs)