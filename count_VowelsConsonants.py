#Count vowels and consonants in string.
#Input: "hello"
#Output:
#Vowels = 2
#Consonants = 3
def VowelsConsonants(s):
    vowels = "aeiouAEIOU"
    vowel_count = 0
    consonant_count = 0
    for char in s:
        if char.isalpha():
            if char in vowels:
                vowel_count += 1
            else:
                consonant_count += 1
    return f"vowels Count: {vowel_count} and Consonant Count: {consonant_count}"

print(VowelsConsonants("Hello"))