class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        import heapq

        h = nums[:k]
        heapq.heapify(h)

        for n in nums[k:]:
            heapq.heappop(h)
            heapq.heappush(h, n)
        
        return heapq.heappop(h)