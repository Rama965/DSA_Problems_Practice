
#Check whether parentheses are balanced.
#Input: "{[()]}"
#Output: True
#Input: "{[(])}"
#Output: False
def valid_parenthesis(s):
    stack = []
    
    mapping = {
        ")":"(",
        "}":"{",
        "]":"["
    }
    
    for char in s:
        
        if char in mapping.values():
            stack.append(char)
            
        elif char in mapping.keys():
            
            if not stack or stack[-1] != mapping[char]:
                return False
            stack.pop()
    return len(stack) == 0

print(valid_parenthesis("()[]{}"))
print(valid_parenthesis("(]"))