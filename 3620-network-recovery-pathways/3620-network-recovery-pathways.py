from collections import deque

class Solution(object):
    def findMaxPathScore(self, edges, online, k):
        n = len(online)
        g = [[] for _ in range(n)]
        indeg = [0] * n
        costs = set()

        for u, v, c in edges:
            g[u].append((v, c))
            indeg[v] += 1
            costs.add(c)

        q = deque()

        for i in range(n):
            if indeg[i] == 0:
                q.append(i)

        topo = []

        while q:
            u = q.popleft()
            topo.append(u)

            for v, _ in g[u]:
                indeg[v] -= 1
                if indeg[v] == 0:
                    q.append(v)

        vals = sorted(costs)

        def check(x):
            dist = [float('inf')] * n
            dist[0] = 0

            for u in topo:
                if dist[u] == float('inf'):
                    continue

                if u != 0 and u != n - 1 and not online[u]:
                    continue

                for v, c in g[u]:
                    if c < x:
                        continue

                    if v != n - 1 and not online[v]:
                        continue

                    dist[v] = min(dist[v], dist[u] + c)

            return dist[n - 1] <= k

        lo, hi = 0, len(vals) - 1
        ans = -1

        while lo <= hi:
            mid = (lo + hi) // 2

            if check(vals[mid]):
                ans = vals[mid]
                lo = mid + 1
            else:
                hi = mid - 1

        return ans