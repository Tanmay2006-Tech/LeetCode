class Solution(object):
    def smallestPalindrome(self, s):
        from collections import Counter

        c=Counter(s)
        left=[]
        mid=""

        for ch in sorted(c):
            left.append(ch*(c[ch]//2))
            if c[ch]%2:
                mid=ch

        left="".join(left)
        return left+mid+left[::-1]