#Sort array using Selection Sort.
#Input: [5,3,8,4,2]
#Output: [2,3,4,5,8]
def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_index = i
        for j in range(i+1,n):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i],arr[min_index] = arr[min_index],arr[i]
    return arr

print(selection_sort([12,34,17,18,29,10]))