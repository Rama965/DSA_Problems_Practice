#Find first index where target appears.
#Input:
#arr = [2,4,4,4,8]
#target = 4

#Output:
#1

def first_occurance_ele(arr,target):
    left = 0
    right = len(arr) - 1
    result = -1
    while left <= right:
        mid = (left + right)//2
        if arr[mid] == target:
            result = mid
            right = mid - 1
        elif arr[mid] < target:
            left = mid+1
        else:
            right = mid - 1
    return result

print(first_occurance_ele([2,4,4,4,8],4))