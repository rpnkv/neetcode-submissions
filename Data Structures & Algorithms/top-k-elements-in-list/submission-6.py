class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        from collections import Counter

        c = Counter(nums)

        import heapq

        nlrgst = heapq.nlargest(k, c.items(), key=lambda t: t[1])

        return [t[0] for t in nlrgst]