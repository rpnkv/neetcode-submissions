class Solution:
    def rob(self, nums: List[int]) -> int:
        a = b = c = d = 0

        for n in nums:
            b, c, d = c, d, max(b,c) + n

        return max(c,d)
