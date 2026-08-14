class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        l = 0
        curr_len = max_len = 1
        nums.sort()

        for r, n in enumerate(nums):
            match n - nums[l]:
                case x if x == 0:
                    continue
                case x if x == 1:
                    curr_len += 1
                    l = r
                case _:
                    l = r
                    curr_len = 1
            
            max_len = max(curr_len, max_len)

        return max_len