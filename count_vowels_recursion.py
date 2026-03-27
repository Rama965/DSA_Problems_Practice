#Count total vowels in a string using recursion.
#Input: "education"
#Output: 5
def count_vowels(s,n):
    vowels = "aeiouAEIOU"
    if n == 0:
        return 0
    count=1 if s[n-1] in vowels else 0
    return count + count_vowels(s,n-1)

print(count_vowels("education",len("education")))