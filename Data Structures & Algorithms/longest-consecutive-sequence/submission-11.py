class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums.sort()

        l = 0 
        seq_len = max_len = int(bool(nums))

        for r, n in enumerate(nums):
            match n - nums[l]:
                case diff if diff == 0:
                    pass
                case diff if diff == 1:
                    l, seq_len = r, seq_len + 1
                case dif if diff > 1:
                    l = r
                    seq_len = 1

            max_len = max(seq_len, max_len)

        return max_len
            

            