class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:

        


        def minCoins(c, n, V):
            t = [[0 if j == 0 else float('inf') - 1 for j in range(V + 1)] for _ in range(n + 1)]

            for i in range(1, n + 1):
                for j in range(1, V + 1):
                    if c[i - 1] <= j:
                        t[i][j] = min(1 + t[i][j - c[i - 1]], t[i - 1][j])
                    else:
                        t[i][j] = t[i - 1][j]

            ans = t[n][V] if t[n][V] != float('inf') - 1 else -1
            return ans
        

        size=len(coins)

        return minCoins(coins,size,amount)