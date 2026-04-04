#Reverse a string using stack.
#Input: hello
#Output: olleh
def reverse_string_usingStack(s):
    stack = []
    
    for char in s:
        stack.append(char)
    
    reversed_string = ""
    while stack:
        reversed_string += stack.pop()
        
    return reversed_string

print(reverse_string_usingStack("hello"))