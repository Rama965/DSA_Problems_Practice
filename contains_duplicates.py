#Contains Duplicate
#Check if array contains duplicate values.
#Input: [1,2,3,4,2]
#Output: True
def contains_duplicates(arr):
    seen = set()
    for num in arr:
        if num in seen:
            return True
        seen.add(num)
    return False

print(contains_duplicates([1,2,3,4,2]))