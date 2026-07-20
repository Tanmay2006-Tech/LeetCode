class Solution:
    def shiftGrid(self, grid, k):
        m,n=len(grid),len(grid[0])
        a=[]
        for r in grid:
            a.extend(r)
        k%=m*n
        a=a[-k:]+a[:-k]
        return [a[i*n:(i+1)*n] for i in range(m)]