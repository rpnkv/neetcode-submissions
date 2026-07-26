class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        nums.sort()

        def dfs(i:int, candidate: list[int], curr_value:int):
            if curr_value == target:
                res.append(candidate.copy())
                return
            
            for j in range(i, len(nums)):
                if curr_value + nums[j] > target:
                    break
                else:
                    candidate.append(nums[j])
                    dfs(j, candidate, curr_value + nums[j])
                    candidate.pop()

        dfs(0, [], 0)
        
        return res