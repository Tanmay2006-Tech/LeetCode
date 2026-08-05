class Solution(object):
    def rotatedDigits(self, n):
        ans=0

        for x in range(1,n+1):
            ok=False
            t=x

            while t:
                d=t%10
                if d in (3,4,7):
                    ok=False
                    break
                if d in (2,5,6,9):
                    ok=True
                t//=10
            else:
                if ok:
                    ans+=1

        return ans