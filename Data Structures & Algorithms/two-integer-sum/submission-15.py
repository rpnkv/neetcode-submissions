class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        visited = {}

        for i, n in enumerate(nums):
            pair = target - n
            if pair in visited:
                return [visited[pair], i]
            else:
                visited[n] = i
            
        