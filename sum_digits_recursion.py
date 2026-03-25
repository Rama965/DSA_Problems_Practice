#Sum of Digits Using Recursion
#Input: 1234
#Output: 10
#1 + 2 + 3 + 4 = 10
def sum_of_digits(n):
    if n == 0:
        return 0
    return n%10 + sum_of_digits(n//10)

print(sum_of_digits(1234))