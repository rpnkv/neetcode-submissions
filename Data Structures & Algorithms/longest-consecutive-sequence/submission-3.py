class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s = set(nums)
        max_len = 0

        for n in s:
            if (n - 1) in s:
                pass
            else:
                len = 1
                while n + 1 in s:
                    len += 1
                    n += 1
                max_len = max(max_len, len)

        return max_len