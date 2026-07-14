def gcd(a,b):
    while b:
        a,b=b,a%b
    return a
class Solution:
    def subsequencePairCount(self, nums):
        MOD=10**9+7
        dp={(0,0):1}
        for x in nums:
            ndp=dp.copy()
            for (a,b),cnt in dp.items():
                na=gcd(a,x) if a else x
                ndp[(na,b)]=(ndp.get((na,b),0)+cnt)%MOD
                nb=gcd(b,x) if b else x
                ndp[(a,nb)]=(ndp.get((a,nb),0)+cnt)%MOD
            dp=ndp
        ans=0
        for (a,b),cnt in dp.items():
            if a and a==b:
                ans=(ans+cnt)%MOD
        return ans