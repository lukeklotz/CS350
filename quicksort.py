
def quicksort(array, lo, hi):
    if hi <= lo: #fully sorted base case
        return
    mid = partition(array, lo, hi) 

    #print(mid)
    #go left
    quicksort(array, lo, mid - 1)

    #go right
    quicksort(array, mid + 1, hi)


def partition(array, lo, hi):
    pivot = array[hi] # choose arbitrary pivot

    pl = lo 
    i  = lo           # search for values LESS THAN pivot

    while i < hi:     # BEGIN searching for values LESS THAN pivot 
        if array[i] < pivot:       # swap
            temp      = array[pl]  # swap code
            array[pl] = array[i]
            array[i]  = temp
            pl += 1                # increment place-holder
        i += 1                     # increment i
    
    #swap the value at array[pl] with the pivot
    array[hi] = array[pl]
    array[pl] = pivot

    return pl

a = [3, 2, 5, 1]

hi = len(a) - 1

quicksort(a, 0, hi)
print(a)
        