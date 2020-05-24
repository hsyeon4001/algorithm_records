#백준 1920번
import sys
n = int(sys.stdin.readline())
a = set(map(int, sys.stdin.readline().split()))
n = int(sys.stdin.readline())
x = list(map(int, sys.stdin.readline().split()))

for i in x:
    if i in a:
        print(1)
    else:
        print(0)