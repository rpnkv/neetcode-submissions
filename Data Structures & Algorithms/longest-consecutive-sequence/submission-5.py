
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums.sort()

        l = 0
        curr_len = max_len = 1 if nums else 0

        for r, num in enumerate(nums):
            match num - nums[l]:
                case diff if diff == 0:
                    pass
                case diff if diff == 1:
                    curr_len += 1
                    max_len = max(max_len, curr_len)
                    l = r
                case diff if diff > 1:
                    curr_len = 1
                    l = r

        return max_len
