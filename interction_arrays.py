#Intersection of Two Arrays
#Find common elements between two arrays.
#Input:
#arr1 = [1,2,2,1]
#arr2 = [2,2]

#Output:
#[2]
def intersection_of_two_arrays(arr1,arr2):
    return list(set(arr1) & set(arr2))

print(intersection_of_two_arrays([1,2,2,1],[2,2]))