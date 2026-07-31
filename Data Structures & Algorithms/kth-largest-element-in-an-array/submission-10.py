class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        import heapq

        h = nums[:k]
        heapq.heapify(h)

        for n in nums[k:]:
            heapq.heappush(h, n)
            heapq.heappop(h)
        
        return heapq.heappop(h)