class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        map1={}
        result=[]

        for i in range(len(nums)):

            compliment= target-nums[i]

            if compliment not in map1:

                map1[nums[i]]=i 
            
            else :
                return [i,map1[compliment]]

        return []
            

        



        