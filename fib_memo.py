




def fib(n, table):


    if n == 0:       # base cases
        return n
    if n == 1:
        return n
    

    # TWO things can happen in the table:
    # 1. It can have values of the fib sequence
    # 2. It can have empty slots (indicated by -1)


    if table[n] != -1:   #  NOT EMPTY. 
        return table[n]  #  Return value in table   
    else:                #  EMPTY.
        table[n] = fib(n-1, table) + fib(n-2, table)  # Add n-1 and n-2 to update the current position in the table
        return table[n]                               # Return the new value
    
n       = 10
table   = [-1] * (n + 1)
res     = fib(n, table)

print(res)