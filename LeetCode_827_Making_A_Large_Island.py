#
# https://leetcode.com/problems/making-a-large-island/
#

def island(grid):
    n = len(grid)
    
    # flatten the array
    grid = [i for y in grid for i in y]
    
    # no land; change one sea to one land
    if not any(grid): 
        return 1
    
    # all land so result is n * n
    if all(grid): 
        return n * n

    # use the union-find algorithm to implement disjoint sets
    # A is the array used for the union-find algorithm
    # S is the size of elements in each distinct whos index is the root of the set
    A = []
    S = []

    # init each element in it's own set
    for y in range(0, n * n):
        A.append(y)
        S.append(1)

    # find root of elem a
    def root(a):
        while  A[a] != a:
            a    = A[a]
            A[a] = A[A[a]]
        return a

    # put a & b in the same set
    def union(a, b):
        a = root(a)
        b = root(b)
        if a != b:
            S[a] += S[b] # recalc. size
            A[b]  = a    # new root
    
    # combine two cells in the same set if both are land
    def comb(a, b):
        if grid[a] == 1 and grid[b] == 1:
            union(a, b)

    # keep a list of coords that are sea cells
    seas = []
    
    # combine all cells that are adjacent land
    for y in range(0, n):
        for x in range(0, n):
            if grid[y * n + x] == 0:
                seas.append((x, y))
                continue
                
            if x != n - 1:
                comb(y       * n + x, y * n + x + 1)
            if y != n - 1:
                comb((y + 1) * n + x, y * n + x    )

    # tmp variable
    maxsize = 0

    # iterate over all sea cells and for each cell find all the land masses connected to it
    # and sum size of all islands if sea changed into land
    # find the cell that produces the maximum score 
    for s in seas:
            x, y = s
            U = set()
            
            for h, v in [(1,0), (-1,0), (0,1), (0,-1)]:
                if 0 <= x + h < n and 0 <= y + v < n:
                    c = (y + v) * n + x + h
                    if grid[c] == 1:
                        U.add(root(c))
                        
            # combine all connected lands into one land mass and compute the total size
            maxsize = max(maxsize, sum(map(lambda x: S[x], U)))

    return maxsize + 1 # + 1 is for sea changed to land

class Solution:
    def largestIsland(self, grid: List[List[int]]) -> int:
        return island(grid)