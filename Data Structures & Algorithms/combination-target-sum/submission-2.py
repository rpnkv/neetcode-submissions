class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        nums.sort()

        def dfs(i: int, curr: list[int], curr_sum: int) -> None:
            if curr_sum == target:
                res.append(curr.copy())
                return

            for j in range(i, len(nums)):
                candidate = nums[j]
                if curr_sum + candidate > target:
                    break
                else:
                    curr.append(candidate)
                    dfs(j, curr, curr_sum + candidate)
                    curr.pop()
            
        
        dfs(0, [], 0)
        return res
