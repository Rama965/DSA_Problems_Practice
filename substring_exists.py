#Check whether substring exists inside string.
#Input:
#string = "datascience"
#substring = "science"

#Output:
#True

def check_substring(string,substring):
    for i in range(len(string) - len(substring) + 1):
        if string[i:i + len(substring)] == substring:
            return True
    return False

print(check_substring("datascience","science"))