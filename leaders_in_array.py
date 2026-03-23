#Find elements greater than all elements to their right.
#Input: [16,17,4,3,5,2]
#Output: [17,5,2]
def leaders(arr):
    result = []
    max_right = arr[-1]
    result.append(max_right)
    for i in range(len(arr)-2,-1,-1):
        if arr[i] > max_right:
            max_right = arr[i]
            result.append(max_right)
    return result[::-1]

print(leaders([19,45,12,4,5,7]))