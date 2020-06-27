# 최대공약수와 최소공배수
def solution(n, m):
    answer = []
    max_v = min(n, m)
    min_v = max(n, m)
    if n == 1 or m == 1:
        answer.append(1)
        answer.append(min_v)
        return answer
        
    while True:
        if n % max_v == 0 and m % max_v == 0:
            answer.append(max_v)
            break
        max_v = max_v - 1

    while True:
        if min_v % n == 0 and min_v % m == 0:
            answer.append(min_v)
            break
        min_v = min_v + 1

    return answer

# 제일 작은 수 제거하기
def solution(arr):
    answer = []
    min_v = 0
    if len(arr) == 1:
        answer.append(-1)
        return answer
    else:
        min_v = min(arr)
    arr.remove(min_v)
    answer = arr
    return answer
print(solution([4,3,2,1]))

# K번째 수
def solution(array, commands):
    answer = []
    for ele in commands:
        i, j, k = ele[0], ele[1], ele[2]
        print(i, j, k)
        result = sorted(array[i-1:j])
        answer.append(result[k-1])
    return answer
array = [1, 5, 2, 6, 3, 7, 4]
commands = [[2, 5, 3], [4, 4, 1], [1, 7, 3]]
print(solution(array, commands))

# 두 정수 사이의 합
def solution(a, b):
    answer = 0
    min_int, max_int = min(a, b), max(a, b)
    while min_int <= max_int:
        answer += min_int
        min_int += 1
    return answer

# 나누어 떨어지는 숫자 배열
def solution(arr, divisor):
    answer = []
    for ele in arr:
        if ele % divisor == 0:
            answer.append(ele)
    if len(answer) == 0:
        answer.append(-1)
    return sorted(answer)

# 약수의 합
def solution(n):
    answer = 0
    i = n
    while i >= 1:
        if n % i == 0:
            answer += i
        i -= 1
    return answer

# 콜라츠 추측
def solution(num):
    answer = 0
    while num > 1 and answer < 501:
        if num % 2 == 1:
            num = num * 3 + 1
        else:
            num = num / 2
        answer += 1
    if num == 1:
        return answer
    elif answer >= 500:
        answer = -1
        return answer

# 같은 숫자는 싫어(미해결)
def solution(arr):
    answer = []
    for i in range(0, len(arr)):
        if i >= len(arr)-1:
            answer = arr
            return answer
        elif arr[i] == arr[i+1]:
            arr.pop(i)
            print(arr, i)


print(solution([1,1,3,3,0,1,1]))