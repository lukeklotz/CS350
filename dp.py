#memoization algorithm
def dp(n, t):

    #global t

    if(t[n] != -1):     #slot with existing information exists
        return t[n]
    
    a = dp(n - 4, t)
    b = dp(n - 3, t)
    c = dp(n - 1, t)
 
    t[n] = 1 + min(a, b, c)
    return t[n]

t = [-1] * 100

t[1] = 1
t[2] = 2
t[3] = 1
t[4] = 1

res = dp(10, t)    

print(res)