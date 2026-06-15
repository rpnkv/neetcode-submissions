class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        for z, num in enumerate(nums):
            if num == 0:
                break

        for n in range(z+1, len(nums)):
            if nums[n] != 0:
                nums[z], nums[n] = nums[n], nums[z]
                z += 1
        

        