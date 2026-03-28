#Sort array using Insertion Sort.
#Input: [5,3,8,4,2]
#Output: [2,3,4,5,8]
def insertion_sort(arr):
    for i in range(1,len(arr)):
        key = arr[i]
        j = i-1
        while j >= 0 and arr[j] > key:
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = key
    return arr
print(insertion_sort([12,17,13,10,9,24]))