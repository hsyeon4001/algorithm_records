# # 최대공약수와 최소공배수
# def solution(n, m):
#     answer = []
#     max_v = min(n, m)
#     min_v = max(n, m)
#     if n == 1 or m == 1:
#         answer.append(1)
#         answer.append(min_v)
#         return answer
        
#     while True:
#         if n % max_v == 0 and m % max_v == 0:
#             answer.append(max_v)
#             break
#         max_v = max_v - 1

#     while True:
#         if min_v % n == 0 and min_v % m == 0:
#             answer.append(min_v)
#             break
#         min_v = min_v + 1

#     return answer

# # 제일 작은 수 제거하기
# def solution(arr):
#     answer = []
#     min_v = 0
#     if len(arr) == 1:
#         answer.append(-1)
#         return answer
#     else:
#         min_v = min(arr)
#     arr.remove(min_v)
#     answer = arr
#     return answer
# print(solution([4,3,2,1]))

# # K번째 수
# def solution(array, commands):
#     answer = []
#     for ele in commands:
#         i, j, k = ele[0], ele[1], ele[2]
#         print(i, j, k)
#         result = sorted(array[i-1:j])
#         answer.append(result[k-1])
#     return answer
# array = [1, 5, 2, 6, 3, 7, 4]
# commands = [[2, 5, 3], [4, 4, 1], [1, 7, 3]]
# print(solution(array, commands))

# # 두 정수 사이의 합
# def solution(a, b):
#     answer = 0
#     min_int, max_int = min(a, b), max(a, b)
#     while min_int <= max_int:
#         answer += min_int
#         min_int += 1
#     return answer

# # 나누어 떨어지는 숫자 배열
# def solution(arr, divisor):
#     answer = []
#     for ele in arr:
#         if ele % divisor == 0:
#             answer.append(ele)
#     if len(answer) == 0:
#         answer.append(-1)
#     return sorted(answer)

# # 약수의 합
# def solution(n):
#     answer = 0
#     i = n
#     while i >= 1:
#         if n % i == 0:
#             answer += i
#         i -= 1
#     return answer

# # 콜라츠 추측
# def solution(num):
#     answer = 0
#     while num > 1 and answer < 501:
#         if num % 2 == 1:
#             num = num * 3 + 1
#         else:
#             num = num / 2
#         answer += 1
#     if num == 1:
#         return answer
#     elif answer >= 500:
#         answer = -1
#         return answer

# # 같은 숫자는 싫어
# def solution(arr):
#     answer = []
#     answer.append(arr[0])
#     for i in range(1, len(arr)):
#         if arr[i] != arr[i-1]:
#             answer.append(arr[i])
#     return answer
# arr = [4,4,4,3,3]
# print(solution(arr))

# # 내 마음대로 정렬하기
# def solution(strings, n):
#     answer = []
#     length = len(strings)
#     if length <= 1:
#         return strings
#     pivot = strings[-1]
#     g1 = []
#     g2 = []
#     for i in range(0, length-1):
#         if strings[i][n] == pivot[n]:
#             if strings[i] < pivot:
#                 g1.append(strings[i])
#             else:
#                 g2.append(strings[i])
#         elif strings[i][n] < pivot[n]:
#             g1.append(strings[i])
#         else:
#             g2.append(strings[i])
#     answer = solution(g1, n) + [pivot] + solution(g2, n)
#     return answer

# # 문자열 내림차순으로 배치하기
# def solution(s):
#     answer = ''
#     up = []
#     low = []
#     for i in s:
#         if i.isupper():
#             up.append(i)
#         else:
#             low.append(i)
#     low.sort()
#     low.reverse()
#     up.sort()
#     up.reverse()
#     result = low + up
#     answer = ''.join(result)
#     return answer

# # 하샤드 수
# def solution(x):
#     answer = True
#     str_x = str(x)
#     arr = list(map(int, str_x))
#     if x % sum(arr) != 0:
#         answer = False
#     return answer

# # 행렬의 덧셈
# def solution(arr1, arr2):
#     answer = [[]]
#     for i in range(len(arr1)):
#         for j in range(len(arr1[i])):
#             arr1[i][j] = arr1[i][j] + arr2[i][j]
            
#     answer = arr1
#     return answer

# # 이상한 문자 만들기
# def solution(s):
#     answer = ''
#     arr = []
#     s = s.split(' ')
#     for word in s:
#         for i in range(0, len(word)):
#             if i % 2 == 0:
#                 word = word[:i] + word[i].upper() + word[i+1:]
#             else:
#                 word = word[:i] + word[i].lower() + word[i+1:]
#         arr.append(word)
#     answer = ' '.join(arr)
#     return answer

# # 자연수 뒤집어 배열로 만들기
# def solution(n):
#     answer = []
#     arr = list(map(int, list(str(n))))
#     answer = list(reversed(arr))
#     return answer

# # 완주하지 못한 선수
# def solution(participant, completion):
#     answer = ''
#     answer_dict = {}
#     arr = participant + completion
#     for p in arr:
#         if p in answer_dict:
#             del answer_dict[p]
#         else:
#             answer_dict[p] = 1

#     answer = list(answer_dict.keys())[0]
#     return answer

# # 모의고사
# def solution(answers):
#     answer = []
#     scores = [0, 0, 0]
#     st1 = [1, 2, 3, 4, 5]
#     st2 = [2, 1, 2, 3, 2, 4, 2, 5]
#     st3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]

#     for i in range(len(answers)):
#         if answers[i] == st1[i % len(st1)]:
#             scores[0] += 1
#         if answers[i] == st2[i % len(st2)]:
#             scores[1] += 1
#         if answers[i] == st3[i % len(st3)]:
#             scores[2] += 1
    
#     max_score = max(scores)
#     for i in range(3):
#         if scores[i] == max_score:
#             answer.append(i + 1)

#     return answer
# print(solution([1,3,2,4,2]))