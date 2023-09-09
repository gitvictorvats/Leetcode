from typing import List

class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:

        def subsetSum(nums, N, sum):

            dp = [[0 for _ in range(sum + 1)] for _ in range(N + 1)]
            dp[0][0] = 1
            
            for i in range(1, N + 1):
                for j in range(sum + 1):
                    dp[i][j] = dp[i-1][j]
                    
                    if j >= nums[i - 1]:
                        dp[i][j] += dp[i-1][j - nums[i - 1]]

            return dp[N][sum]

        total = sum(nums)
        
        # Check if it's even possible to partition the numbers into two subsets to reach the target sum
        if (total + target) % 2 == 1 or total < abs(target):
            return 0
        
        new_sum = (total + target) // 2
        N = len(nums)
        
        return subsetSum(nums, N, new_sum)
