class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        s = {}
        

        for i, n in enumerate(nums):
            n_pair = target - n

            if n_pair in s:
                return sorted([i, s[n_pair]])
            else:
                s[n] = i
        
        raise Exception('unexpexted state')

                