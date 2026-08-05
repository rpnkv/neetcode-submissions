class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        mask = 0xFFFF

        for n in nums:
            mask ^= n

        return 0xffff ^ mask

