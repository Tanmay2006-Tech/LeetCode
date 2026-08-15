class Solution:
    def longestSubsequence(self,nums):
        x=0
        for n in nums:
            x^=n
        if x:
            return len(nums)
        for n in nums:
            if n:
                return len(nums)-1
        return 0