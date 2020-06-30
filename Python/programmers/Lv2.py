# 탑
def solution(heights):
    answer = []
    
    while heights:
        p = heights.pop()
        for i in range(len(heights), 0, -1):
            if heights[i-1] > p:
                answer.append(i)
                break
            if i-1 == 0:
                answer.append(0)
    answer.append(0)
    answer = list(reversed(answer))
    return answer
print(solution([3, 9, 9, 3, 5, 7, 2]))

# 프린터
def solution(priorities, location):
    answer = 0
    wait = list(range(0, len(priorities)))
    printed = []

    while wait:
        d = priorities.pop(0)
        w = wait.pop(0)
        if len(priorities) <= 0:
            printed.append(w)
            answer = printed.index(location) + 1
            return answer
        if d >= max(priorities):
            printed.append(w)
        else:
            priorities.append(d)
            wait.append(w)
print(solution([1, 1, 9, 1, 1, 1], 0))

# 기능개발
import math
def solution(progresses, speeds):
    answer = []
    days = []
    for i in range(len(progresses)):
        day = math.ceil((100 - progresses[i]) / speeds[i])
        days.append(day)

    while days:
        x = 1
        n = days.pop(0)
        if len(days) < 1:
            answer.append(x)
            break
        for i in range(len(days)):
            if n >= days[0]:
                x += 1
                days.pop(0)
        answer.append(x)
    return answer

# 124 나라의 숫자
def solution(n):
    answer = ''
    while n:
        n, d = divmod(n, 3)
        answer = '412'[d] + answer
        if not d:
            n -= 1
    return answer

# 피보나치 수
def solution(n):
    answer = 0
    a, b = 0, 1
    for i in range(n):
        a, b = b, a+b
    answer = a % 1234567
    return answer

# JadenCase 문자열 만들기
def solution(s):
    answer = ''
    s = s.split(' ')

    for i in s:
        i = i.capitalize()
        answer += i + ' '
    return answer[:-1]
