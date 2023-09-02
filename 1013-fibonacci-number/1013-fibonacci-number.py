class Solution:

    #Recursion without memoization
    # def fib(self, n: int) -> int:

    #     if n==0 :
    #         return 0
        
    #     if n==1 or n==2:
    #         return 1

    #     else:
    #         return self.fib(n-1)+self.fib(n-2)

     #Recursion with memoization

    def fib(self, n: int) -> int:

        if n==0 :
            return 0
        
        if n==1:
            return 1

        arr=[-1]*(n+1)
        arr[0]=0
        arr[1]=1


        if arr[n]!=-1:
            return arr[n]

        arr[n]= self.fib(n-1)+self.fib(n-2)

        return arr[n]
        