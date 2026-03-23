#Find longest word in sentence.
def longest_word(sentence):
    words = sentence.split()
    long_word = words[0]
    for word in words:
        if len(word) > len(long_word):
            long_word = word
    return long_word

print(longest_word("I love programming"))
print(longest_word("Now Ai is ruling the world"))