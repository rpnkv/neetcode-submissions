class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) < 2:
            return sum(nums)
        else:
            return nums[0] + self.rob(nums[2:])