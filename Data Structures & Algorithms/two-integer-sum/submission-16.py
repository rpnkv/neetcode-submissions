class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        visited = {}

        for i, n in enumerate(nums):
            expected = target - n
            if expected in visited:
                return [visited[expected], i]
            else:
                visited[n] = i
        
        raise NotImplemetedError