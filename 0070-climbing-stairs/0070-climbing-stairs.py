class Solution:
    def climbStairs(self, n: int) -> int:
        dic=dict()
        def climb(n):
            if n==1:
                return 1
            elif n ==2:
                return 2
            else:
                if n in dic:
                    return dic[n]
                else:
                    dic[n] = climb(n-1) + climb(n-2)
                    return dic[n]
        
        return climb(n)