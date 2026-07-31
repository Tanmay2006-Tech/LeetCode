class Solution(object):
    def minimumPushes(self, word):
        from collections import Counter
        f=sorted(Counter(word).values(),reverse=True)
        ans=0
        for i,x in enumerate(f):
            ans+=x*(i//8+1)
        return ans