# 10818 번
len = int(input())
nums = list(map(int, input().split()))
print(min(nums), max(nums))

# 2562번
nums = []
for i in range(9):
    nums.append(int(input()))
print(max(nums))
print(nums.index(max(nums))+1)

# 2577번
nums = []
for i in range(3):
    nums.append(int(input()))
result = nums[0]
for i in range(1, len(nums)):
    result = result * nums[i]
for i in range(0, 10):
    print(str(result).count(str(i)))

# 3052번
nums = []

for i in range(10):
    nums.append(int(input()) % 42)
nums = list(set(nums))
print(len(nums))

# 1546번
a = int(input())
nums = list(map(int, input().split()))
max_num = max(nums)
total = 0
for index, value in enumerate(nums):
    nums[index] = nums[index] / max_num * 100
print(sum(nums) / len(nums))

# 8958번
n = int(input())
for i in range(n):
    total = 0
    save = 1
    answer = input()
    for j in range(len(answer)):
        if answer[j] == 'O':
            total += save
            save += 1
        elif answer[j] == 'X':
            save = 1
    print(total)

# 4344번
case = int(input())
for j in range(case):
    score = list(map(int, input().split()))
    n = score.pop(0)
    average = sum(score) / n
    count = 0
    for i in score: 
        if i > average:
            count += 1
    answer = round(count / n * 100, 3)
    print('%.3f' % answer + '%')