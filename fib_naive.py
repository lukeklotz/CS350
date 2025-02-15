
#0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597...

#naive approach

def fib(n, total_calls):

    if n == 0:          # base cases
        return 0
    if n == 1:
        return 1
    
    total_calls[0] += 1 # tracking total number of calls
    return fib(n-1, total_calls) + fib(n-2, total_calls)

total_calls = [0]       # keeping track of total calls for fun
n           = 11        # nth fib number

print(f"{n}th fib number is {fib(n, total_calls)}") 
print(f"and it took your computer {total_calls[0]} operations to find it") 