class Solution:
    def rob(self, nums: List[int]) -> int:

        n=len(nums)
        memo=[-1 for i in range (0,n)]

        def rob(nums,n):

            if n==1 :
                return nums[0]

            if n==2:
                return max(nums[0], nums[1])

            
            if memo[n-1] !=-1:
                return memo[n-1]

            include= rob(nums,n-2)+nums[n-1]
            exclude= rob(nums,n-1)
            
            memo[n-1]=max(include,exclude)

            return memo[n-1]

        return rob(nums,n)

        
        