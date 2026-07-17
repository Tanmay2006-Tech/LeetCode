from bisect import bisect_left
class Solution:
    def gcdValues(self, nums, queries):
        m=max(nums)
        freq=[0]*(m+1)
        for x in nums:
            freq[x]+=1
        cnt=[0]*(m+1)
        for i in range(1,m+1):
            for j in range(i,m+1,i):
                cnt[i]+=freq[j]
        pairs=[0]*(m+1)
        for i in range(m,0,-1):
            pairs[i]=cnt[i]*(cnt[i]-1)//2
            for j in range(i*2,m+1,i):
                pairs[i]-=pairs[j]
        pre=[]
        val=[]
        s=0
        for i in range(1,m+1):
            if pairs[i]:
                s+=pairs[i]
                pre.append(s)
                val.append(i)
        ans=[]
        for q in queries:
            ans.append(val[bisect_left(pre,q+1)])
        return ans