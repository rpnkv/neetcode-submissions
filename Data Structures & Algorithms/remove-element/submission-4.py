class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        l = 0

        for r, n in enumerate(nums):
            if n != val:
                nums[l] = n
                l += 1

        return l 