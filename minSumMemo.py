

def minMemo(arr, i, j, table):
    if table == None:               #initialize empty dict
        table = {}
    
    if (i, j) in table:             #if tuple (i, j) exists, return its value
        return table[(i, j)]
    
    if i == len(arr) - 1:           #out of bounds base case
        return arr[i][j]

    a = minMemo(arr, i + 1, j, table)      #get value of downward path
    b = minMemo(arr, i + 1, j + 1, table)  #get value of diagonal right path

    table[(i, j)] = min(a,b) + arr[i][j]   #initialize index (i, j) with result
    return table[(i, j)]


arr = [[5, 0, 0, 0],
       [3, 4, 0, 0],
       [8, 3, 6, 0],
       [3, 2, 2, 9]]

print(minMemo(arr, 0, 0, table=None))