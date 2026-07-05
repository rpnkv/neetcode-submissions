class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        n_len = len(nums)

        s_max = min(nums)

        for i in range(n_len):
            start_sum = nums[i]
            for j in range(i + 1, n_len):
                # for j in range(i + 1, n_len + 1):
                # s_max = max(s_max, sum(nums[i:j])) # very
                start_sum += nums[j]
                s_max = max(start_sum, s_max)

            s_max = max(start_sum, s_max)

        return s_max