#Check if an array is sorted in ascending order using recursion.
#Input: [1,2,3,4,5]
#Output: True
#Input: [1,3,2,4,5]
#Output: False
def is_sorted(arr,n):
    if n==0 or n==1:
        return True
    if arr[n-2] > arr[n-1]:
        return False
    return is_sorted(arr,n-1)

print(is_sorted([1,2,3,4,5],5))
print(is_sorted([5,4,3,2,1],5))