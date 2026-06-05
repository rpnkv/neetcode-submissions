class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) < 2:
            return sum(nums)
        else:
            return max(
                nums[0] + self.rob(nums[2:]),
                nums[1] + self.rob(nums[3:]),
                )   