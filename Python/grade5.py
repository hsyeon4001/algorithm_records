# 10039번
score = []
for i in range(5):
    i = int(input())
    if i < 40:
        score.append(40)
    else:
        i = int(i)
        score.append(i)
print( int(sum(score) / len(score)) )

# 5543번
burger = []
drink = []
for i in range(3):
    i = int(input())
    burger.append(i)
for i in range(2):
    i = int(input())
    drink.append(i)
print(min(burger) + min(drink) - 50)

# 10817번
a = list(map(int, input().split()))
def second_num(arr):
    sorted_nums = sorted(arr, reverse=True)
    return sorted_nums[1]
print(second_num(a))