class Solution(object):
    def gcdSum(self, nums):
        def gcd(a,b):
            while b:
                a,b=b,a%b
            return a
        arr=[]
        mx=0
        for x in nums:
            if x>mx:
                mx=x
            arr.append(gcd(x,mx))
        arr.sort()
        ans=0
        i,j=0,len(arr)-1
        while i<j:
            ans+=gcd(arr[i],arr[j])
            i+=1
            j-=1
        return ans