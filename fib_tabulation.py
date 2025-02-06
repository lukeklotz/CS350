
#0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597...

#tabulation soltion

def fib(n):

    if n == 0:
        return 0
    if n == 1:
        return 1
    
    res = [0] * (n + 1)
    res[1] = 1

    #assume i is 2 for first iteration
    for i in range(2, n):
        print(res[i])
        res[i] = res[i-1] + res[i-2] 
        i = i + 1
    
    return res[n - 1]

print(fib(8))