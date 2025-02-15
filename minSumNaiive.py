
def minSum(arr, i, j):
    if i == len(arr) - 1:            #out of bounds base case
       return arr[i][j]

    #check for smallest num
    a = minSum(arr, i + 1, j)        #look down
    b = minSum(arr, i + 1, j + 1)    #look diagonal right

    return min(a, b) + arr[i][j]     #return smallest num plus current num
    

arr = [[5, 0, 0, 0],
       [3, 4, 0, 0],
       [8, 3, 6, 0],
       [3, 2, 2, 9]]

print(minSum(arr, 0, 0))
