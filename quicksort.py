
def quicksort(array, lo, hi):
    if hi <= lo:
        return
    mid = partition(array, lo, hi)

    #go left
    quicksort(array, lo, mid - 1)

    #go right
    quicksort(array, mid + 1, hi)


def partition(array, lo, hi):

    pivot = array[hi]

    pl = lo
    i = lo

    while i < hi:
        if array[i] < pivot:
            temp = array[pl]
            array[pl] = array[i]
            array[i] = temp
            pl += 1
        i += 1
    
    #swap the vlaue at array[pl] with the pivot
    array[hi] = array[pl]
    array[pl] = pivot

    return pl

a = [10, 5, 2, 6, 7, 3, 12, 4, 7, 4]

hi = len(a) - 1

quicksort(a, 0, hi)
print(a)
        