import math
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:

      sum= 0
      maxm=nums[0]
       
      for i in range(len(nums)):

              sum=nums[i]+sum
              maxm=max(maxm,sum)
       
              if sum < 0:
                  
                  sum=0                 
        
      return maxm
               

              

