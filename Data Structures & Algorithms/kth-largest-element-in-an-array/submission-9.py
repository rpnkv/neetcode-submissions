class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        import heapq

        i = heapq.nlargest(k, nums)

        return i[-1]