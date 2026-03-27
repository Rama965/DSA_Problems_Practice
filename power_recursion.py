#Calculate a^b using recursion.
#Input: a=2, b=3
#Output: 8
def power(a,b):
    if b == 0:
        return 1
    return a * power(a,b-1)

print(power(2,3))