# # 10039번
# score = []
# for i in range(5):
#     i = int(input())
#     if i < 40:
#         score.append(40)
#     else:
#         i = int(i)
#         score.append(i)
# print( int(sum(score) / len(score)) )

# # 5543번
# burger = []
# drink = []
# for i in range(3):
#     i = int(input())
#     burger.append(i)
# for i in range(2):
#     i = int(input())
#     drink.append(i)
# print(min(burger) + min(drink) - 50)

# # 10817번
# a = list(map(int, input().split()))
# def second_num(arr):
#     sorted_nums = sorted(arr, reverse=True)
#     return sorted_nums[1]
# print(second_num(a))

# # 2523번
# n = int(input())
# star = '*'
# for i in range(n):
#     print(star)
#     star += '*'
# for i in range(n, 0, -1):
#     print(star[0:i-1])

# # 2446번
# n = int(input())
# for i in reversed(range(1, n+1)):
#     print(' ' * (n-i) + '*' * (2*i-1))
# for i in range(2, n+1):
#     print(' ' * (n-i) + '*' * (2*i-1))

# 10996번
n = int(input())
for i in range(n):
    if n == 1:
        print('*')
    else:
        if n % 2 == 1:
            print('*' + ' *' * int(n / 2) + '\n' + ' *' * int(n / 2))
        else:
            print('*' + ' *' * ((n / 2)-1) + '\n' + ' *' * int(n / 2))
