#Reverse a string without using built-in reverse.
#h
#eh
#leh
#lleh
#olleh

def reverse(s):
    reversed = ""
    for char in s:
        reversed = char + reversed
    return reversed

print(reverse("hello"))