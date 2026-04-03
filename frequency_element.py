#Frequency of Elements
#Count frequency of each element.
#Input: [1,2,2,3,1]
#Output:
#1 → 2
#2 → 2
#3 → 1
def frequency_element(arr):
    freq = {}
    for num in arr:
        freq[num] = freq.get(num,0)+1
    return freq

print(frequency_element([1,2,2,3,1]))