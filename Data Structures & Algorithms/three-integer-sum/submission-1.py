class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        results = set()
        nums.sort()

        for l in range(len(nums) - 2):
            for m in range(l + 1, len(nums) - 1):
                for r in range(m + 1, len(nums)):
                    if nums[l] + nums[m] + nums[r] == 0:
                        results.add((nums[l], nums[m], nums[r]))

        return [list(t) for t in results]
