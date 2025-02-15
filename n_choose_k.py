
def f(n, k, table):

    if (table[n][k] != -1):
        return table[n][k]
    
    a = f(n-1, k-1, table)
    b = f(n-1, k, table)

    table[n][k] = a + b

    return table[n][k]


# time complexity O(n*k)