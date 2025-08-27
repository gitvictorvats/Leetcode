from collections import Counter

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        temp1=Counter(s)
        temp2=Counter(t)

        print(temp1)
        print(temp2)

        return temp1==temp2

        