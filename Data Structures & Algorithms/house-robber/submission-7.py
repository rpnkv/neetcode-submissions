class Solution:
    def rob(self, nums: List[int]) -> int:
        res = []

        for i in range(len(nums)):
            sub2 = 0 if i - 2 < 0 else res[i - 2]
            sub3 = 0 if i - 3 < 0 else res[i - 3]

            res.append(nums[i] + max(sub2, sub3))

        return max(res[-2:])