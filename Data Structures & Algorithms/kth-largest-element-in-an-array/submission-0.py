class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        import heapq

        lrg = heapq.nlargest(k, nums)

        l = heapq.heappop_max(lrg)
        for _ in range(1, k):
            l = heapq.heappop_max(lrg)

        return l