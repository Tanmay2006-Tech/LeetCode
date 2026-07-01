from collections import deque
import heapq
class Solution:
    def maximumSafenessFactor(self, grid):
        n=len(grid)
        dist=[[-1]*n for _ in range(n)]
        q=deque()
        for i in range(n):
            for j in range(n):
                if grid[i][j]:
                    dist[i][j]=0
                    q.append((i,j))
        d=[(1,0),(-1,0),(0,1),(0,-1)]
        while q:
            x,y=q.popleft()
            for dx,dy in d:
                nx,ny=x+dx,y+dy
                if 0<=nx<n and 0<=ny<n and dist[nx][ny]==-1:
                    dist[nx][ny]=dist[x][y]+1
                    q.append((nx,ny))
        pq=[(-dist[0][0],0,0)]
        vis={(0,0)}
        while pq:
            safe,x,y=heapq.heappop(pq)
            safe=-safe
            if x==n-1 and y==n-1:
                return safe
            for dx,dy in d:
                nx,ny=x+dx,y+dy
                if 0<=nx<n and 0<=ny<n and (nx,ny) not in vis:
                    vis.add((nx,ny))
                    heapq.heappush(pq,(-min(safe,dist[nx][ny]),nx,ny))