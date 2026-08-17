from functools import cache

class Solution:
    def stoneGameV(self,stoneValue):
        n=len(stoneValue)
        s=[0]*(n+1)
        for i,x in enumerate(stoneValue):
            s[i+1]=s[i]+x

        @cache
        def dfs(l,r):
            if l>=r:
                return 0
            ans=0
            left=0
            right=s[r+1]-s[l]

            for i in range(l,r):
                left+=stoneValue[i]
                right-=stoneValue[i]

                if left<right:
                    if ans>=left*2:
                        continue
                    ans=max(ans,left+dfs(l,i))
                elif left>right:
                    if ans>=right*2:
                        break
                    ans=max(ans,right+dfs(i+1,r))
                else:
                    ans=max(ans,left+dfs(l,i),right+dfs(i+1,r))

            return ans

        return dfs(0,n-1)