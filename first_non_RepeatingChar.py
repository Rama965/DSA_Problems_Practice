#First Non-Repeating Character
#Find first character that appears only once.
#Input: "swiss"
#Output: w

def first_non_repeating(s):
    frequency = {}
    for char in s:
        frequency[char] = frequency.get(char,0) + 1
    
    for char in s:
        if frequency[char] == 1:
            return char
    return None

print(first_non_repeating("swiss"))