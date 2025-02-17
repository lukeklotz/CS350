

def generate_shifted_arr(num_elements, num_shifts):

    i = num_shifts
    res = []
    while i < num_elements:
        res.append(i)
        i += 1

    i = 0
    while i < num_shifts:
        res.append(i) 
        i += 1

    return res

arr = generate_shifted_arr(8, 2)
print(arr)