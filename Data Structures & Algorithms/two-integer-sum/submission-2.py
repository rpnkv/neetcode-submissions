class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        s = set(nums)

        for i, n in enumerate(nums):
            if target - n in s:
                if n * 2 == target:
                    nums.remove(n)
                    return [n, nums.index(n + 1)]
                else:
                    return [i, nums.index(target - n)]

        
        raise Exception('unexpected state')


        