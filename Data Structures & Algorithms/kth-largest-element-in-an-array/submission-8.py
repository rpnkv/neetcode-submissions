class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        import heapq

        h = nums[:k]
        heapq.heapify(h)

        for n in nums[k:]:
            #heapq.heappush(h, n)
            #heapq.heappop(h)
            heapq.heappushpop(h, n)
            #heapq.heapreplace(h, n)

        return heapq.heappop(h)