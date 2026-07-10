class Counter:
    def __init__(self):
        self.counts = {}
        self.total_count = 0

    def add(self, char:str) -> None:
        cnt = self.counts
        if char not in cnt:
            cnt[char] = 0
        
        cnt[char] += 1
        self.total_count += 1

    def count_infrequents(self) -> int:
        cnt = self.counts
        if len(cnt) < 2:
            return 0
        else:
            return self.total_count - max(cnt.values())

    def remove(self, char: str) -> None:
        cnt = self.counts
        if cnt[char] < 1:
            del cnt[char]
        else:
            cnt[char] -= 1
        self.total_count -= 1


class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = max_len = 0
        cnt = Counter()

        for r, char in enumerate(s):
            cnt.add(char)
            
            while cnt.count_infrequents() > k:
                cnt.remove(s[l])
                l += 1
            
            max_len = max(max_len, cnt.total_count)

        return max_len

