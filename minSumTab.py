

def tab(arr, table, i, j):

    #base case. return result
    if i <= 0 and j <= 0:
        return arr[0][0] + min(table[i+1][j], table[i+1][j+1]) 
    
    #initialize bottom row of table
    #note that i STARTS at 3
    if i == 3:                               
        while j >= 0:
            table[i][j] = arr[i][j]
            j -= 1   #move backwards along the bottom row
        i -= 1 # move to next row up
        j = 3  # reset j  

    #update table
    if arr[i][j] != 0:    # check if we're inside the triangle        
        a = table[i+1][j]     # check down
        b = table[i+1][j+1]   # check down->right
        table[i][j] = min(a, b) + arr[i][j] 

    else:
        return tab(arr, table, i, j - 1)     # if outside triangle, iterate j backwards

    if j <= 0:
        return tab(arr, table, i - 1, 3)     # last column, move to row - 1

    return tab(arr, table, i, j - 1)         # iterate column

arr = [[1, 0, 0, 0],
       [3, 1, 0, 0],
       [1, 1, 1, 0],
       [1, 5, 2, 5]]

table = [[0, 0, 0, 0],
         [0, 0, 0, 0],
         [0, 0, 0, 0],
         [0, 0, 0, 0]]

print(tab(arr, table, 3, 3))