class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        res = {0:0}
        coins.sort()

        for v in range(amount + 1):
            for c in coins:
                if c > v:
                    break
                
                if v - c in res:
                    res[v] = min(1 + res[v - c], res.get(v, math.inf))
                
            
        return res.get(amount, -1)

        