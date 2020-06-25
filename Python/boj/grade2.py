#1330번
a = list(map(int, input("").split(" ")))
if a[0] > a[1]:
    print('>')
elif a[0] < a[1]:
    print('<')
else:
    print('==')

#9498번
a = int(input(""))
if 90 <= a <= 100:
    print('A')
elif 80 <= a <= 89:
    print('B')
elif 70 <= a <= 79:
    print('C')
elif 60 <= a <= 69:
    print('D')
else:
    print('F')

# 2753번
a = int(input(""))
if a % 4 == 0 : 
    if a % 100 != 0 or a % 400 == 0 :
        print(1)
    else :
        print(0)
else :
    print(0)

# 14681번
x, y = int(input("")), int(input(""))
if x > 0 and y > 0 :
    print(1)
elif x < 0 and y < 0 : 
    print(3)
elif x > 0 and y < 0 :
    print(4)
else :
    print(2)

# 2884번
a = list(map(int, input("").split(" ")))
h, m = a[0], a[1]

if m >= 45:
    print(h, m-45)
else:
    if h != 0:
        print(h-1, m+15)
    else:
        print(23, m+15)