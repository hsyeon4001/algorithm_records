# p51 2-4-1 팩토리얼1
def fact(n):
    f = 1
    for i in range(1, n+1):
        f = f * i
    return f
print(fact(1))
print(fact(5))
print(fact(10))

# p53 2-4-3 재귀호출
def hello():
    print('hello')
    hello()
hello()

# p56 2-4-3 팩토리얼2
def fact(n):
    if n <= 1:
        return 1
    return n * fact(n-1)

print(fact(1))
print(fact(5))
print(fact(10))

p59 2-4 연습문제
def sum(n):
    if n <= 1:
        return 1
    return n + sum(n-1)
print(sum(100))

def find_max(arr, n):
    if n == 1:
        return arr[0]
    max_v = find_max(arr, n-1)
    if max_v > arr[n-1]:
        return max_v
    else:
        return arr[n-1]
arr = [1, 9, 3, 24, 86]
print(find_max(arr, len(arr)))

# p61 2-5-1 최대공약수
def gcd(a, b):
    i = min(a, b)
    while True:
        if a % i == 0 and b % i == 0:
            return i
        i = i - 1
print(gcd(12, 8))

# p62 2-5-2 유클리드
def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)
print(gcd(12, 7))

# p66 2-5 연습문제(피보나치)
def fibo(n):
    if n <= 1:
        return n
    return fibo(n-2) + fibo(n-1)
print(fibo(7))
print(fibo(10))

# p75 2-6 하노이의탑
def hanoi(n, from_pos, to_pos, aux_pos):
    if n == 1:
        return print(from_pos, '->', to_pos)
    hanoi(n-1, from_pos, aux_pos, to_pos)
    print(from_pos, '->', to_pos)
    hanoi(n-1, from_pos, to_pos, aux_pos)
hanoi(2, 1, 3, 2)
print(solution(3, 12))
