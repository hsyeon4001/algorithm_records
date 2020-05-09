#10172번
print("""\
|\_/|
|q p|   /}
( 0 )\"\"\"\\
|"^"`    |
||_/=\\\\__|\
""")

#1000번
#1) map 함수 사용 (M 29380KB, T 64ms, C 59B)
a = list(map(int, input("").split(" ")))
print(a[0] + a[1])

#2) 리스트 내포(List comprehension) (M 29380KB, T 64ms, C 83B)
a = input("").split(" ")
list_a = [int (i) for i in a]
print(list_a[0] + list_a[1])

#10869번
a = list(map(int, input("").split(" ")))
print(a[0] + a[1])
print(a[0] - a[1])
print(a[0] * a[1])
print(int(a[0] / a[1]))
print(a[0] % a[1])

#10430번
a = list(map(int, input("").split(" ")))

print( (a[0] + a[1] ) % a[2] )
print( ((a[0] % a[2]) + (a[1] % a[2])) % a[2] )
print( (a[0] * a[1]) % a[2] )
print( ((a[0] % a[2]) * (a[1] % a[2])) % a[2] )

#2588번
a, b = int(input("")), int(input(""))
print(a * (b % 10))
print(a * ((b % 100) // 10))
print(a * (b // 100))
print(a * b)