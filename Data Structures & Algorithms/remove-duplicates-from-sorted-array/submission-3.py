class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        l = 0

        for r, n in enumerate(nums):
            if nums[l] != n:
                l += 1
                nums[l], nums[r] = nums[r], nums[l]
        
        return l + 1