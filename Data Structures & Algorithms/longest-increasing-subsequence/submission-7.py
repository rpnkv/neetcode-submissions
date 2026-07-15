class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        lens = [1] * len(nums)

        for i, n in enumerate(nums):
            for j in range(i+1, len(nums)):
                if n < nums[j]:
                    lens[j] = max(lens[j], lens[i] + 1)

        return max(lens)