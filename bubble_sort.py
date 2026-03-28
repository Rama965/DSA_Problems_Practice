#Sort an array using Bubble Sort.
#Input: [5,3,8,4,2]
#Output: [2,3,4,5,8]
def bubblesort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0,n-i-1):
            if arr[j] > arr[j+1]:
                arr[j],arr[j+1] = arr[j+1],arr[j]
    return arr

print(bubblesort([11,10,9,34,52,19]))