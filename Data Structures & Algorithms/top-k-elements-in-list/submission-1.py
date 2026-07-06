import heapq
from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        c = Counter(nums)

        freq = heapq.nlargest(k, c.items(), key=lambda item: item[1])

        return freq