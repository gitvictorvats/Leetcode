class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:

        def minCoins(c, n, V, memo):
            if V == 0:
                return 0
            if n == 0:
                return float('inf')
            if memo[n][V] != -1:
                return memo[n][V]

            if c[n - 1] <= V:
                memo[n][V] = min(1 + minCoins(c, n, V - c[n - 1], memo), minCoins(c, n - 1, V, memo))
            else:
                memo[n][V] = minCoins(c, n - 1, V, memo)
            
            return memo[n][V]

        size = len(coins)
        memo = [[-1 for _ in range(amount + 1)] for _ in range(size + 1)]
        
        result = minCoins(coins, size, amount, memo)
        return result if result != float('inf') else -1
