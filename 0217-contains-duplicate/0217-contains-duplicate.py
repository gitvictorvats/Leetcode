class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:

        temp={}

        for i in nums:

            if i in temp.keys():

                temp[i]+=1
            
            else:
                
                temp[i]=1

        print(str(temp))

        for i in temp.values():

            print(i)
            if i !=1:
              return True
        
        return False
        
        