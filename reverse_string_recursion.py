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