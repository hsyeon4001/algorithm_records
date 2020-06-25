import math

#p14
def abs_sign(a):
    if a >= 0:
        return a
    else:
        return -a

def abs_square(a):
    b = a * a
    return math.sqrt(b)

print(abs_sign(5))
print(abs_sign(-3))
print()
print(abs_square(5))
print(abs_square(-3))

#p24 1-1-3
def sum_n(n):
    s = 0
    for i in range(1, n+1):
        s = s + i
    return s
print(sum_n(100))

def sum_n(n):
    return n * (n+1) // 2
print(sum_n(100))

# p32 연습문제
def sol(n):
    answer = 0
    for i in range(1, n+1):
        i = i * i
        answer += i
    return answer
print(sol(10))

# p36 1-2 리스트 최댓값 구하기
def find_max(a):
    max_v = a[0]
    for i in range(1, len(a)):
        if max_v < a[i]:
            max_v = a[i]
    return max_v
v = [17, 92, 18, 33, 58, 7, 33]
print(find_max(v))

def find_index(a):
    max_i = 0
    for i in range(1, len(a)):
        if a[max_i] < a[i]:
            max_i = i
    return max_i
v = [4, 23, 82, 54, 3]
print(find_index(v))

# p39 1-2 연습문제(최솟값 구하기)
def find_min(arr):
    min = arr[0]
    n = len(arr)
    for i in range(1, n):
        if min > arr[i]:
            min = arr[i]
    return min
v = [4, 23, 82, 54, 3]
print(find_min(v))

# p41 1-3 집합
def find_same_name(a):
    n = len(a)
    result = set()
    for i in range(0, n-1):
        for j in range(i+1, n):
            if a[i] == a[j]:
                result.add(a[i])
    return result
name = ["Tom", "Jerry", "Mike"]
print(find_same_name(name))

# p47 1-3-1 연습문제
def solution(arr):
    n = len(arr)
    result = set()
    for i in range(0, n-1):
        for j in range(i+1, n):
            print(arr[i], arr[j])
solution(["Tom", "Jerry", "Mike"])
