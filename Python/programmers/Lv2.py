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

# 더 맵게
import heapq
def solution(scoville, K):
    answer = 0
    heap = []
    for num in scoville:
        heapq.heappush(heap, num)
    
    while heap[0] < K:
        try:
            heapq.heappush(heap, heapq.heappop(heap) + (heapq.heappop(heap) * 2))
        except IndexError:
            return -1
        answer += 1
    return answer
print(solution([1,2,3,9,10,12], 7))

# 소수 찾기
from itertools import permutations
def solution(numbers):
    answer = 0
    arr = []
    for i in range(len(numbers)):
        a = list(permutations(numbers, i+1))
        arr += [int(''.join(i)) for i in a]
    for i in set(arr):
        b = 0
        for j in range(1, i+1):
            if i % j == 0 and i != 0:
                b += 1
            if b >= 3:
                break
        if b == 2:
            answer += 1
    return answer
print(solution("011"))

# 큰 수 만들기
def solution(number, k):
    answer = ''
    numbers = list(map(int, number))
    arr = sorted(numbers)
    for i in range(k):
        numbers.remove(arr[i])
    answer = ''.join(str(numbers))[1:-1].replace(', ', '')
    return answer
print(solution('1924', 2))

# 전화번호 목록
def solution(phone_book):
    answer = True
    phone_book.sort()

    for i in range(len(phone_book)-1):
        if phone_book[i] in phone_book[i+1]:
            answer = False
            break
    return answer

# 위장
def solution(clothes):
    answer = 1
    dic = dict()

    for name, kind in clothes:
        if kind not in dic:
            dic[kind] = 1
        else:
            dic[kind] += 1
    
    for val in dic.values():
        answer *= (val + 1)
    
    answer = answer - 1
    return answer
clothes = [["yellow_hat", "headgear"], ["blue_sunglasses", "eyewear"], ["green_turban", "headgear"]]
solution(clothes)

# 카펫
def solution(brown, yellow):
    answer = []
    y_div = []
    y_div2 = []
    for i in range(1, yellow+1):
        if yellow % i == 0:
            y_div.append(i)
    
    for i in y_div:
        for j in y_div:
            if i * j == yellow and i >= j:
                y_div2.append((i, j))
    
    for a, b in y_div2:
        if (a+1) * 2 + (b+1) * 2 == brown:
            answer = [a+2, b+2]
            return answer
print(solution(24, 24))

# 체육복
def solution(n, lost, reserve):
    answer = 0
    set_reserve = set(reserve) - set(lost)
    set_lost = set(lost) - set(reserve)
    for i in set_reserve:
        if i-1 in set_lost:
            set_lost.remove(i-1)
        elif i+1 in set_lost:
            set_lost.remove(i+1)
    answer = n - len(set_lost)
    return answer
print(solution(3, [3], [1]))

----------------------------------여기까지 노트 등록함
# 타겟 넘버
def solution(numbers, target):
    answer = 0
    arr = [0]
    for i in numbers:
        arr2 = []
        for j in arr:
            arr2.append(j+i)
            arr2.append(j-i)
        arr = arr2
    answer = arr.count(target)
    return answer
print(solution([1, 1, 1, 1, 1], 3))


# 스킬트리
def solution(skill, skill_trees):
    answer = len(skill_trees)
    skill_idx = [None] * len(skill)
    new_trees = []
    for tree in skill_trees:
        for i in tree:
            if i not in skill:
                tree = tree.replace(i, '')
        new_trees.append(tree)

    for tree in new_trees:
        for i in range(len(tree)):
            if tree[i] != skill[i]:
                answer -= 1
                break
    return answer
solution("CBD", ["BACDE", "CBADF", "AECB", "BDA"])

# # 다리를 지나는 트럭(미해결)
# def solution(bridge_length, weight, truck_weights):
#     answer = 1
#     bridge1 = [truck_weights[0]]
#     bridge2 = {truck_weights[0]:1}
#     fin = []
#     weight2 = weight

#     while bridge1:
#         for w, l in bridge2.items():
#             if w < weight2:
#                 print(w, l)
#                 weight2 -= w        
#                 l += 1
#                 print(bridge2, weight2)
#             break
#     return answer
# print(solution(2, 10, [7, 4, 5, 6]))

# 가장 큰 수
def solution(numbers):
    answer = ''
    numbers = list(map(str, numbers))
    numbers.sort(key=lambda x:x*3, reverse=True)
    answer = str(int(''.join(numbers)))
    return answer

# # 영어 끝말잇기(미해결)
# def solution(n, words):
#     answer = []
#     word_dict = {words[0]:1}
#     last = words[0][-1]
#     chk = ''
#     words2 = words.copy()
#     words2.pop(0)

#     for word in words2:
#         if word[0] != last:
#             chk = word
#         else:
#             last = word[-1]
#             chk = last
#         if word in word_dict:
#             word_dict[word] += 1
#         else:
#             word_dict[word] = 1
    
#     word_tuples = sorted(word_dict.items(), key=lambda x: x[1], reverse=True)

#     if word_tuples[0][1] == 2:
#         # 2 찾기
#         chk = word_tuples[0][0]
#         for i, v in enumerate(words):
#             if v == chk:
#                 idx = i
#     elif len(chk) > 1:
#     # chk 찾기
#         idx = words.index(chk)
#     else:

#         answer = [0, 0]
#         print(answer)
#         return answer
#     a, b = divmod(idx, n)
#     print(idx, a, b)
#     answer = [b+1, a+1]
#     print(answer)
#     return answer
# solution(3, ["tank", "kick", "know", "wheel", "land", "dream", "mother", "robot", "tank"])
# solution(5, ["hello", "observe", "effect", "take", "either", "recognize", "encourage", "ensure", "establish", "hang", "gather", "refer", "reference", "estimate", "executive"])
# solution(2, ["hello", "one", "even", "never", "now", "world", "draw"])