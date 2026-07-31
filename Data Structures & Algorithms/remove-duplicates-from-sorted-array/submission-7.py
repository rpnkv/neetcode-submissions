class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        l = 0

        for n in nums[1:]:
            if n != nums[l]:
                l += 1
                nums[l] = n
            
        return l + 1