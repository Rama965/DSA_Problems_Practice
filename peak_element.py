def peak_element(arr):
    left = 0
    right = len(arr) - 1
    while left < right:
        mid = (left + right) // 2
        if arr[mid] < arr[mid+1]:
            left = mid + 1
        else:
            right = mid
    return left

print(peak_element([1,3,20,4,1,0]))