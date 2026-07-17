class Counter:
    def __init__(self):
        self.d = {}
        self.total_count = 0
    
    def add(self, char: s) -> None:
        if not char in self.d:
            self.d[char] = 0
        
        self.d[char] += 1
        self.total_count += 1
    
    def remove(self, char:s) -> None:
        if self.d[char] == 1:
            del self.d[char]
        else:
            self.d[char] -= 1
        
        self.total_count -= 1
    
    def number_of_infrequent(self) -> int:
            return self.total_count - max(self.d.values())


class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l, max_len, counter = 0, 0, Counter()

        for r, char in enumerate(s):
            counter.add(char)

            while counter.number_of_infrequent() > k:
                counter.remove(s[l])
                l += 1
            
            max_len = max(max_len, r - l + 1)
        
        return max_len
