class Solution:
    def longestRepeating(self,s,queryCharacters,queryIndices):
        n=len(s)
        size=1
        while size<n:
            size*=2
        t=[None]*(2*size)

        for i,c in enumerate(s):
            t[size+i]=(c,c,1,1,1,1)

        for i in range(size-1,0,-1):
            t[i]=self.merge(t[2*i],t[2*i+1])

        ans=[]

        for c,p in zip(queryCharacters,queryIndices):
            i=size+p
            t[i]=(c,c,1,1,1,1)
            i//=2

            while i:
                t[i]=self.merge(t[2*i],t[2*i+1])
                i//=2

            ans.append(t[1][4])

        return ans

    def merge(self,a,b):
        if a is None:
            return b
        if b is None:
            return a

        lc1,rc1,p1,s1,m1,l1=a
        lc2,rc2,p2,s2,m2,l2=b

        lc=lc1
        rc=rc2
        p=p1
        s=s2
        m=max(m1,m2)

        if rc1==lc2:
            m=max(m,m1 if l1==p1 else 0,s1+p2)
            if p1==l1:
                p=l1+p2
            if s2==l2:
                s=s1+l2

        return (lc,rc,p,s,m,l1+l2)
