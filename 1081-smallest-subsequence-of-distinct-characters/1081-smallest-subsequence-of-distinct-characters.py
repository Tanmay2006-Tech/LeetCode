class Solution:
    def smallestSubsequence(self, s):
        last={c:i for i,c in enumerate(s)}
        st=[]
        vis=set()
        for i,c in enumerate(s):
            if c in vis:
                continue
            while st and st[-1]>c and last[st[-1]]>i:
                vis.remove(st.pop())
            st.append(c)
            vis.add(c)
        return "".join(st)