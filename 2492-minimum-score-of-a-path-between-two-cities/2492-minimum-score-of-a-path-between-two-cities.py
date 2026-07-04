from collections import deque

class Solution:
    def minScore(self, n, roads):
        g=[[] for _ in range(n+1)]

        for u,v,w in roads:
            g[u].append((v,w))
            g[v].append((u,w))

        q=deque([1])
        vis={1}
        ans=float('inf')

        while q:
            u=q.popleft()

            for v,w in g[u]:
                ans=min(ans,w)

                if v not in vis:
                    vis.add(v)
                    q.append(v)

        return ans