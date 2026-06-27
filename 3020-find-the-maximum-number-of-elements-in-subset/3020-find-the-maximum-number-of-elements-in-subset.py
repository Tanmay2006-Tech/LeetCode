from collections import Counter

class Solution:
    def maximumLength(self, nums):
        cnt=Counter(nums)
        ans=1

        if 1 in cnt:
            ans=max(ans,cnt[1] if cnt[1]%2 else cnt[1]-1)

        for x in cnt:
            if x==1:
                continue

            cur=0
            y=x

            while cnt.get(y,0)>=2:
                cur+=2
                if y*y not in cnt:
                    cur-=1
                    break
                y*=y

            if cnt.get(y,0)==1:
                cur+=1
            elif cnt.get(y,0)==0:
                cur-=1

            ans=max(ans,max(cur,1))

        return ans