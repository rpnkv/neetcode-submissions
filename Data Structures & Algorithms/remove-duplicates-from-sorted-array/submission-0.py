class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        l = 0
        for r, num in enumerate(nums):
            if num == nums[l]:
                continue
            else:
                l += 1
                nums[l], nums[r] = nums[r], nums[l]

        return l + 1