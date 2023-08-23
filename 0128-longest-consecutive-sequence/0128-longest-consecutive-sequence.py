class Solution:
    global count
    def longestConsecutive(self, nums: List[int]) -> int:

        nums = set(nums)

        ans = 0

        for num in nums:

            if num - 1 not in nums:
                this_num = num
                count = 1

                while this_num + 1 in nums:
                    count += 1
                    this_num += 1
            
                ans = max(ans, count)
        
        return ans

            

                
        
            
            


            

        


        



        

            

                
        
            
            


            

        


        