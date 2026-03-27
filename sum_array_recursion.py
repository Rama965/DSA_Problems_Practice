#Find sum of elements in an array using recursion.
#Input: [1,2,3,4,5]
#Output: 15
def sum_array(arr,n):
    if n == 0:
        return 0
    return arr[n-1] + sum_array(arr,n-1)

print(sum_array([1,2,3,4,5],5))