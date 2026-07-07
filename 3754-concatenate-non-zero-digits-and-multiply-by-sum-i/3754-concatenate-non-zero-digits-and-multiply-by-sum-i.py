class Solution(object):
    def sumAndMultiply(self, n):
        x=""
        s=0

        for c in str(n):
            if c!="0":
                x+=c
                s+=int(c)

        if x=="":
            return 0

        return int(x)*s