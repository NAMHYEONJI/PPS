def islandPerimeter(grid):
    """
    :type grid: List[List[int]]
    :rtype: int
    """
    cnt = 0
    h = len(grid)
    if h == 0: 
        return 0 

    w = len(grid[0])

    for i in range(h):
        for j in range(w):
            if grid[i][j] == 1:
                cnt += 4
                if i-1 >= 0 and grid[i-1][j] == 1:
                    cnt -= 2
                if j-1 >= 0 and grid[i][j-1] == 1:
                    cnt -= 2
    return cnt

grid = [[1,0]]
print(islandPerimeter(grid))