# 10952번
while sum != 0:
    arr = list(map(int, input().split()))
    sum = arr[0] + arr[1]
    if sum == 0:
        break
    print(sum)

# 10951번
import sys
while True:
    try:
        a, b = map(int, sys.stdin.readline().split())
        print(a+b)
    except:
        break

# 1110번
num = int(input())
n = num
chk = ''
i = 0
while chk != num :
    chk = int(str(n % 10) + str((n // 10 + n % 10) % 10))
    n = chk
    i += 1
print(i)