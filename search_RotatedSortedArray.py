#Search in Rotated Sorted Array
#Search element in rotated sorted array.
#Input: [4,5,6,7,0,1,2]
#Target = 0
#Output = index 4
def search_rotated(arr,target):
    left = 0
    right = len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[left] <= arr[mid]:
            if arr[left] <= target < arr[mid]:
                right = mid - 1
            else:
                left = mid + 1
        else:
            if arr[mid] <= target < arr[right]:
                left = mid + 1
            else:
                right = mid - 1
    return -1

print(search_rotated([4,5,6,7,0,1,2],0))