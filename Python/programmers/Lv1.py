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