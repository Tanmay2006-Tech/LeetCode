class Solution:
    def sequentialDigits(self, low, high):
        s="123456789"
        ans=[]
        for l in range(len(str(low)),len(str(high))+1):
            for i in range(10-l):
                num=int(s[i:i+l])
                if low<=num<=high:
                    ans.append(num)
        return ans