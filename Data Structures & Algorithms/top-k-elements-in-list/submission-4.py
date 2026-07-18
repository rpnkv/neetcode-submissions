class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        import heapq
        from collections import Counter

        counts = Counter(nums)

        return [key for key, value in heapq.nlargest(k, counts.items(), key=lambda x: x[1])]