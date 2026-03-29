#Quick Sort
#Choose pivot element
#Place pivot at correct position
#Put smaller elements left
#Put larger elements right
#Repeat recursively
# Example
#[5,3,8,4,2]
#Pivot = 5
#Left = [3,4,2]
#Right = [8]
#Sort left again

def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[0]
    left = [x for x in arr[1:] if x <= pivot]
    right = [x for x in arr[1:] if x > pivot]
    return quick_sort(left) + [pivot] + quick_sort(right)

print(quick_sort([5,3,8,4,2]))