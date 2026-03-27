#Print numbers from 1 to N using recursion.
#Input: 5
#Output: 1 2 3 4 5
def print_numbers(n):
    if n == 0:
        return
    print_numbers(n-1)
    print(n,end=" ")

print(print_numbers(5))