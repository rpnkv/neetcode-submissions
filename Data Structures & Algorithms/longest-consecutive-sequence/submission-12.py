class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums.sort()

        l = 0
        ln = ln_max = 0 if not nums else 1

        for r, num in enumerate(nums):
            if num != nums[l]:
                if num == nums[l] + 1:
                    ln += 1
                else:
                    ln = 1

                l = r

            ln_max = max(ln_max, ln)

        return ln_max