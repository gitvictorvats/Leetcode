class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:

        last_day=days[len(days)-1]

        memo=[-1]*(last_day+1)

        myset=set(days)
        print(myset)

        def solve(days,costs,curr_day,memo):

            if curr_day > last_day :
                return 0
            
            if curr_day not in myset:

                return solve(days,costs,curr_day+1,memo)

            if memo[curr_day]!=-1:
                return memo[curr_day]

            one_day=costs[0]+solve(days,costs,curr_day+1,memo)
            one_week=costs[1]+solve(days,costs,curr_day+7,memo)
            one_month=costs[2]+solve(days,costs,curr_day+30,memo)

            memo[curr_day]=min(one_day,one_week,one_month)
            return memo[curr_day]


        return solve(days,costs,1,memo)







    


        

        
        

                