import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freqs = {}

        for n in nums:
            if n not in freqs:
                freqs[n] = 0
            
            freqs[n] += 1
        
        freqs = [(freq, num) for num, freq in freqs.items()]
        heapq.heapify_max(freqs)

        res = []

        for _ in range(k):
            res.append(heapq.heappop_max(freqs)[1])
        
        return res