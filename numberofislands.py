


def numberofislands(m):
    if not m:
        return 0
    
    rows = len(m)
    cols = len(m[0])

    visited = set()   # stores unique elements
    islands = 0

    def explore(r, c): #dfs algorithm

        if (r < 0 or         # base cases 
            c < 0 or
            r >= rows or
            c >= cols or
            m[r][c] == 0
            or (r,c) in visited):

            return
        
        visited.add((r, c))

        explore(r+1, c) #down
        explore(r-1, c) #up
        explore(r, c+1) #right
        explore(r, c-1) #left


    for r in range(rows):
        for c in range(cols):
            if m[r][c] == 1 and (r, c) not in visited:
                islands += 1
                explore(r, c) # visits the rest of the island and tracks indicies
                
    return islands

m = [[0,1,0,0],
     [1,1,0,0],
     [0,0,0,1],
     [1,0,0,0]]

m2 = [[1]]

m3 = [[0,1,1,1,
      1,1,1,1,
      1,1,1,1]]

m4 = [[1,0,0,1,0]]

m5 = [[1,1,0,0,0],
      [0,0,1,0,0],
      [0,1,0,1,0],
      [0,0,0,1,0]]

print(numberofislands(m5))