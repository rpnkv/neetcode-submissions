class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        import heapq

        h = heapq.nlargest(k, nums)

        res = h[0]
        
        for _ in range(k):
            res = heapq.heappop_max(h)

        return res