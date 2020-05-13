# 2739번
a = int(input(""))
for i in range(1, 10):
    print(a, '*', i, '=', a * i)

# 10950번
len = int(input(""))
for i in range(len):
    a, b = map(int, input("").split(" "))
    print(a+b)
    
# 8393번
n = int(input(""))
list = []
for i in range(1, n+1):
    list.append(i)
print(sum(list))

# 15552번
import sys
len = int(input())
for i in range(len):
    a, b = map(int, sys.stdin.readline().split())
    print(a + b)

# 2741번
n = int(input())
for i in range(1, n+1):
    print(i)

# 2742번
n = int(input())
for i in range(n, 0, -1):
    print(i)

# 11021번
import sys
len = int(input())
for i in range(1, len+1):
    a, b = map(int, sys.stdin.readline().split())
    print("Case #{}: {}".format(i, a+b))

# 11022번
import sys
len = int(input())
for i in range(1, len+1):
    a, b = map(int, sys.stdin.readline().split())
    print("Case #{}: {} + {} = {}".format(i, a, b, a+b))

# 2438번
len = int(input())
for i in range(1, len+1):
    print("*" * i)

# 2439번
len = int(input())
for i in range(1, len+1):
    print(' '*(len - i) + '*'*i)

# 10871번
a = list(map(int, input().split()))
arr = list(map(int, input().split()))
answer = []
for ele in arr:
    if a[1] > ele:
        answer.append(str(ele))
print(" ".join(answer))