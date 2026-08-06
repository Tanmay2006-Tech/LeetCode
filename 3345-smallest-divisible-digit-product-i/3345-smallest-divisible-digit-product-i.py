class Solution(object):
    def smallestNumber(self, n, t):
        while True:
            p=1
            for d in str(n):
                p*=int(d)
            if p%t==0:
                return n
            n+=1