class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums.sort()

        max_len = 1 if nums else 0

        l = 0
        for r, n in enumerate(nums):
            if nums[l] == n:
                continue
            elif nums[l] + 1 == n:
                max_len = max(r - l + 1, max_len)
                l = r
            else:
                l = r

        return max_len