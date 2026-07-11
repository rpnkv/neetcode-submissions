import heapq
from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        return [t[0] for t in heapq.nlargest(k, Counter(nums).items(),key=lambda x: x[1])]