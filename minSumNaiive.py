
def minSum(arr, i, j):
    if i == len(arr) - 1:            #out of bounds base case
       return arr[i][j]

    #check for smallest num
    a = minSum(arr, i + 1, j)        #look down
    b = minSum(arr, i + 1, j + 1)    #look diagonal right

    return min(a, b) + arr[i][j]     #return smallest num plus current num
    

arr = [[1, 0, 0, 0],
       [3, 1, 0, 0],
       [8, 3, 1, 0],
       [3, 2, 2, 1]]

print(minSum(arr, 0, 0))
