



nums = [6, 7, 1, 2, 3, 4, 5]

#nums = [0, 1, 2, 4, 5, 6, 7]

#nums = [30, 40, 50, 66, 78, 11, 24]

#nums = [5, 6, 7, 8, 9, 10, 1, 2, 3, 4]

#nums = [-5000, -4000, -3000, -2000, -1000, 0, 1000, 2000, 3000]

#nums = [2, 3, 4, 5, 6, 6, 7, 8, 9, 0, 1]

#nums = [1]


def findMin(nums):
    e = len(nums) - 1
    s = 0
    #mid = (e + s) // 2
 
    #array is rotated len(nums) - 1 amount of times
    #which means the array is sorted and first element is lowest
    if nums[s] <= nums[e]:
        return s

    while s < e:
        mid = (s + e) // 2

        if s == mid or e == mid: # base case (mid has to be either e or s)
            if nums[s] < nums[e]: # in this case, either s or e is the smallest, so we check both
                return s
            if nums[s] > nums[e]:
                return e
        if nums[s] > nums[mid]: # lowest in 2nd half
            e = mid
        if nums[s] < nums[mid]: # lowest in 1st half
            s = mid
    

print(findMin(nums))
        