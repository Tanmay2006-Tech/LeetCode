class Solution(object):
    def maxProduct(self, n):
        d=list(map(int,str(n)))
        ans=0
        for i in range(len(d)):
            for j in range(i+1,len(d)):
                ans=max(ans,d[i]*d[j])
        return ans