class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        cache = [amount+1] * (amount+1)
        cache[0] = 0
        for amt in range(1, amount+1):
            for c in coins:
                if (amt - c) >= 0:
                    cache[amt] = min(cache[amt], 1 + cache[amt-c])

        return cache[amount] if cache[amount] != amount + 1 else -1