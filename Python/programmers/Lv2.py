# # 탑
# def solution(heights):
#     answer = []
    
#     while heights:
#         p = heights.pop()
#         for i in range(len(heights), 0, -1):
#             if heights[i-1] > p:
#                 answer.append(i)
#                 break
#             if i-1 == 0:
#                 answer.append(0)
#     answer.append(0)
#     answer = list(reversed(answer))
#     return answer
# print(solution([3, 9, 9, 3, 5, 7, 2]))

