
#Check whether parentheses are balanced.
#Input: "{[()]}"
#Output: True
#Input: "{[(])}"
#Output: False
def valid_parenthese(s):
    stack = []
    mapping = {
        ')' : '(',
        '}' : '{',
        ']' : '['
    }
    for char in s:
        if char in mapping.values():
            stack.append(char)
        elif char in mapping.keys():
            if stack == []:
                return False
            if mapping[char] != stack.pop():
                return False
    return stack == []

print(valid_parenthese("{[()]}"))
print(valid_parenthese("{[(])}"))