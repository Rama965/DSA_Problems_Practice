#Find maximum element in array using recursion.
#Input: [2, 9, 4, 7, 1]
#Output: 9
def max_array(arr,n):
    if n == 1:
        return arr[0]
    return max(arr[n-1], max_array(arr,n-1))

print(max_array([12,15,10,39,14,3],6))