#Count how many times each character appears in a string.
def char_freq(s):
    freq = {}
    for char in s:
        freq[char] = freq.get(char,0) + 1
    return freq

print(char_freq("Apple"))