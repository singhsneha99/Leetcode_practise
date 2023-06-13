class Solution(object):
    def equalPairs(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        count=0
        l=len(grid)
        rgrid=[]
        cgrid=[]
        for i in range(l):
            col=[]
            for j in range(l):
                row=grid[i]
                col.append(grid[j][i])
            rgrid.append(row)
            cgrid.append(col)
        #print("r:",rgrid)
        #print("c:",cgrid)
        for k in range(l):
            for m in range(l):
                if(rgrid[k]==cgrid[m]):
                    count=count+1
        return count
