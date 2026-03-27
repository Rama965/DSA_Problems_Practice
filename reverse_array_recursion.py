#Reverse an array in-place using recursion.
#Input: [1,2,3,4,5]
#Output: [5,4,3,2,1]
def reverse_array(arr,start,end):
    if start >= end:
        return
    arr[start],arr[end] = arr[end],arr[start]
    return reverse_array(arr,start+1,end-1)

arr=[12,13,10,9,14]
reverse_array(arr,0,len(arr)-1)
print(arr)