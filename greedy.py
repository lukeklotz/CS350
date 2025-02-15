
#greedy algorithm

def greedy(n):
    #greedy(n - 4) 4 coin
    #greedy(n - 3) 3 coin
    #greedy(n - 1) 1 coin

    if(n==4 or n==3 or n==1):
        return 1
    if(n==2):
        return 2

    a = greedy(n - 4)
    b = greedy(n - 3)
    c = greedy(n - 1)
    
    min = a
    if(b < min):
        min = b
    if(c < min):
        min = c
    
    return min + 1

res = greedy(47)    # this input takes 5 minutes !!

print(res)

                    # time complexity = O(3^n)