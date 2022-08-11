def solution(grid):
    rows = grid
    cols = zip(*grid)
    subs = []
    
    for i in range(0,7,3):
        for j in range(0,7,3):
            subs.append([grid[r][c] for r in range(i, i+3) for c in range(j,j+3)])
    
    def isvalid(arr):
        nums = [x for x in arr if str.isdigit(x)]
        return len(nums) == len(set(nums))
    
    return all([
        all(map(isvalid, rows)),
        all(map(isvalid, cols)),
        all(map(isvalid, subs))
    ])
    
    

