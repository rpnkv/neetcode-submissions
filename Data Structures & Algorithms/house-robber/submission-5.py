class Solution:
    def rob(self, nums: List[int]) -> int:
        res = [0] * len(nums)

        for i in range(len(nums)):
            prev = res[i - 2] if i - 2 >= 0 else 0
            prev_2 = res[i - 3] if i - 3 >= 0 else 0

            res[i] = nums[i] + max(prev, prev_2)
            print(i, res)

        return max(res[-1], res[-2] if len(nums) > 1 else 0)
