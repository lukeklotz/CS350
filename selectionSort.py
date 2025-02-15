

#nums = [5, 1, 3, 4, 10]

nums = [6, 4, 2, 7, 9, 12, 4, 1, 0, 2, 1, 5, 45, 2, 7, 3]

n = len(nums)

def selecSort(nums, n):
    smallest = 0

    for smallest in range(smallest, n):
        i = smallest + 1
        for i in range(i, n):
            if nums[i] < nums[smallest]:
                temp = nums[smallest]
                nums[smallest] = nums[i]
                nums[i] = temp
            #i = i + 1
        #smallest = smallest + 1

    return nums

print(selecSort(nums, n))
        


        
