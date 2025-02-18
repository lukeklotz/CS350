

def tab(arr, table, i, j):

        

    if i <= 0 and j <= 0:
        table[0][0] = arr[0][0] + min(table[i+1][j], table[i+1][j+1])
        print(table)
        return table[0][0]
    
    if i == 3: #initialize bottom row
        while j >= 0:
            table[i][j] = arr[i][j]
            j -= 1
        i -= 1
        j = 3

    if arr[i][j] != 0:
        #print(arr[i][j])
        a = table[i+1][j]
        b = table[i+1][j+1]
        table[i][j] = min(a, b) + arr[i][j]

    else:
        return tab(arr, table, i, j - 1)

    if j <= 0:
        return tab(arr, table, i - 1, 3)

    return tab(arr, table, i, j - 1)






arr = [[1, 0, 0, 0],
       [3, 1, 0, 0],
       [1, 1, 3, 0],
       [1, 1, 2, 5]]


table = [[0, 0, 0, 0],
         [0, 0, 0, 0],
         [0, 0, 0, 0],
         [0, 0, 0, 0]]



print(tab(arr, table, 3, 3))