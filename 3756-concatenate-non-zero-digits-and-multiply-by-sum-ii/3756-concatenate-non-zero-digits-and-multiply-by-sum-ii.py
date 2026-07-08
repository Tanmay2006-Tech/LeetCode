from bisect import bisect_left,bisect_right
class Solution(object):
    def sumAndMultiply(self, s, queries):
        mod=10**9+7
        pos=[]
        dig=[]
        for i,c in enumerate(s):
            if c!='0':
                pos.append(i)
                dig.append(ord(c)-48)
        m=len(dig)
        pw=[1]*(m+1)
        for i in range(1,m+1):
            pw[i]=pw[i-1]*10%mod
        pre=[0]*(m+1)
        sm=[0]*(m+1)
        for i,d in enumerate(dig):
            pre[i+1]=(pre[i]*10+d)%mod
            sm[i+1]=sm[i]+d
        ans=[]
        for l,r in queries:
            a=bisect_left(pos,l)
            b=bisect_right(pos,r)-1
            if a>b:
                ans.append(0)
                continue
            length=b-a+1
            x=(pre[b+1]-pre[a]*pw[length])%mod
            ssum=sm[b+1]-sm[a]
            ans.append(x*ssum%mod)
        return ans