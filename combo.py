

# n choose k 'naive' solution

def f(n, k):
    
    if n == k:
        return 1
    if k == 1:
        return n
    if k == 0:
        return 1
    
    return f(n-1, k-1) + f(n-1, k)


print(f(25, 10))