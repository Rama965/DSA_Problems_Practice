def first_occurance(arr,target):
    left = 0
    right = len(arr)-1
    result = -1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            result = mid
            right = mid-1
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return result

def last_occurance(arr,target):
    left = 0
    right = len(arr) - 1
    result = -1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            result = mid
            left = mid + 1
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return result

def count_occurance(arr,target):
    first = first_occurance(arr,target)
    last = last_occurance(arr,target)

    if first == -1:
        return 0
    return last - first + 1

arr = [2,4,4,4,6,8]
print(count_occurance(arr,4))
