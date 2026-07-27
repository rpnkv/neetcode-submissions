class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        from collections import Counter
        import heapq

        c = Counter(nums)

        res = heapq.nlargest(k, c.items(), key=lambda t: t[1])

        return [k for k, v in res]