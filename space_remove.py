#Remove all spaces from string.
def remove_space(s):
    result = ""
    for char in s:
        if char != " ":
            result += char
    return result

print(remove_space("Hello world"))