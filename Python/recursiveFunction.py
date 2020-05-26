#백준 10872
n = int(input())

def factorial_recursive(n):
    if n > 1:
        return n * factorial_recursive(n-1)
    else:
        return 1
print(factorial_recursive(n))