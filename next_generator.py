#Find next greater element for each element in array.

#Example:
#Input: [4,5,2,10]
#Output:
#4 → 5
#5 → 10
#2 → 10
#10 → -1
def next_generator(arr):
    stack = []
    result = [-1] * len(arr)
    
    for i in range(len(arr)):
        
        while stack and arr[i] > arr[stack[-1]]:
            index = stack.pop()
            result[index] = arr[i]
        stack.append(i)
    return result

print(next_generator([4,5,2,10]))