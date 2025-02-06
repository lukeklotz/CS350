

arr = [10, 5, 1, 2, 800, 0]

target = 10
size = len(arr)

def search(arr, target, size) -> bool:
    i = 0
    while i < size:
        if arr[i] == target:
            return True
        i = i + 1
    
    return False


if search(arr, target, size) == True:
    print("target found")
else:
    print("target missing")



#runtime -> O(n)
    
    

