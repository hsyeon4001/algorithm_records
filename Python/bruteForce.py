n = int(input())
case = []
for i in range(n):
    a, b = map(int, input().split())
    case.append([a, b])

answer = []
for i in range(len(case)):
    cnt = 1
    for j in range(len(case)):
        if case[i][0] < case[j][0] and case[i][1] < case[j][1]:
            cnt += 1
    answer.append(cnt)

for i in answer:
    print(i, end=' ')