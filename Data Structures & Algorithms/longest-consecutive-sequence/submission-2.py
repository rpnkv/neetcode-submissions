class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s = set(nums)

        max_len = 0

        for n in nums:
            if not (n - 1) in s:
                curr_len = 1
                while (n + 1) in s:
                    curr_len += 1
                    n += 1
                max_len = max(max_len, curr_len)

        return max_len