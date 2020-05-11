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
