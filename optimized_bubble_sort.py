#Optimized Bubble Sort
#Why optimize?
#Normal Bubble Sort still checks even when array becomes sorted early.
#Optimized version stops early.
def Optimized_Bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        swapped = False
        for j in range(0,n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1],arr[j]
                swapped = True
        if not swapped :
            break
    return arr

#print(Optimized_Bubble_sort([17,10,45,12,24]))
print(Optimized_Bubble_sort([1,2,3,4,5]))