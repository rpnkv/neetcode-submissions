class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums.sort()

        max_len = 1 if nums else 0

        l, ln = 0, 1

        for r, n in enumerate(nums):
            if nums[l] == n:
                continue
            elif nums[l] == n - 1:
                ln += 1
                l = r
                max_len = max(ln, max_len)
            else:
                l = r
                ln = 1
        return max_len