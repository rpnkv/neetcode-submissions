class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums.sort()
        
        l, r = 0, len(nums) - 1

        while l < r:
            match (nums[l] + nums[r]):
                case x if x == target:
                    return [l,r]
                case x if x < target:
                    l+=1
                case _:
                    r-=1
        
        raise Exception('unexpected state')


        