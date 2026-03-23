#Find the element that appears more than n/2 times in the array
#Increase count if same element
#Decrease count if different
#Reset candidate when count becomes 0
def majority_element(arr):
    count = 0
    candidate = None
    for num in arr:
        
        if count == 0:
            candidate = num
        
        if num == candidate:
            count += 1
        else:
            count -= 1
    return candidate

print(majority_element([3,3,4,2,3,3,3]))