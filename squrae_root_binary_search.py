#Square Root Using Binary Search
#Find square root of a number (floor value).
#Input: 16 → Output: 4
#Input: 20 → Output: 4
def square_root(n):
    left = 0
    right = n
    answer = 0
    while left <= right:
        mid = (left + right) // 2
        if mid * mid == n:
            return mid
        elif mid * mid < n:
            answer = mid
            left = mid + 1
        else:
            right = mid - 1
    return answer

print(square_root(25))