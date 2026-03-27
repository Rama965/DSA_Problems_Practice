#Reverse String Using Recursion
#Input: hello
#Output: olleh
#reverse("hello")
#= reverse("ello") + h
#= reverse("llo") + e + h
#= reverse("lo") + l + e + h
#= reverse("o") + l + l + e + h
#= o + l + l + e + h
def reverse_string(s):
    if len(s) == 0:
        return s
    return reverse_string(s[1:]) + s[0]

print(reverse_string("rama"))

#Reverse a String Using Recursion (Array Approach)
def reverse_string_array(s,start,end):
    if start >= end:
        return
    s[start],s[end] = s[end],s[start]
    return reverse_string_array(s,start+1,end-1)

s = list("hello")
reverse_string_array(s,0,len(s)-1)
print("".join(s))