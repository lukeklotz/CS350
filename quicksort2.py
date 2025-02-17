

def q(array, lo, hi):
    if hi <= lo: # base case
        return

    mid = partition(array, lo, hi) 

    q(array, lo, mid - 1)

    q(array, mid + 1, hi)


def partition(array, lo, hi):

    pivot = array[hi]

    i  = lo
    pl = lo

    while i < hi:
        if array[i] < pivot:
            temp      = array[pl]          # swap
            array[pl] = array[i]
            array[i]  = temp
            pl += 1
        i += 1

    array[hi] = array[pl]
    array[pl] = pivot

    return pl


a = [3, 2, 6, 12, 3, 5]
hi = len(a) - 1

q(a, 0, hi)
print(a)