import math
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        
        max_val = float('-inf')
        ln = len(nums)
        curr = max_val
        for idx in range(ln):
            if curr + nums[idx] < nums[idx]:
                curr = nums[idx]
            else:
                curr += nums[idx]
            max_val = max(max_val, curr)
        return max_val
      

              


