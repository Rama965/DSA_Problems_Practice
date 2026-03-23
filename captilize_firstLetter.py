#Capitalize First Letter of Each Word
def captilize_words(sentence):
    words = sentence.split()
    result = ""
    for word in words:
        result += word[0].upper() + word[1:] + " "
    return result

print(captilize_words("hi how are you"))
