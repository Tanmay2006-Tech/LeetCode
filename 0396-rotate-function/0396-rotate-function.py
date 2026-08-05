class Solution(object):
    def maxRotateFunction(self, nums):
        n=len(nums)
        s=sum(nums)
        f=sum(i*x for i,x in enumerate(nums))
        ans=f

        for i in range(n-1,0,-1):
            f=f+s-n*nums[i]
            ans=max(ans,f)

        return ans