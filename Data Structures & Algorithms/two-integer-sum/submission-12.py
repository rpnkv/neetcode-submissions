class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        s = {}

        for i,n in enumerate(nums):
            pair = target - n

            if pair in s:
                return (s[pair], i)
            else:
                s[n] = i
        