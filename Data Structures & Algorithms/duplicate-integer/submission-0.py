class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        s = set()

        for n in nums:
            if n in nums:
                return True
            else:
                s.add(n)

        return False