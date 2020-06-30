text = ['   + -- + - + -   ',
'   + --- + - +   ',
'   + -- + - + -   ',
'   + - + - + - +   ']

# 1)
arr = []
for i in text:
    arr.append(chr(int(i.strip().replace(' ', '').replace('+', '1').replace('-', '0'), 2)))
print(''.join(arr))

# 2)
print(''.join([chr(int(i.strip().replace(' ', '').replace('+', '1').replace('-', '0'), 2)) for i in text]))

# ord(): 문자 -> 숫자
# chr(): 숫자 -> 문자 
# list comprehension : [i(실행문) for i in range(10)] 간결한 코드로 리스트 생성 가능
# print([f'{i} X {j} = {i*j}' for i in range(2, 10) for j in range(1, 10)]) : list comprehension 사용한 구구단
# zfill(): 자리수 맞추기
# print('111'.zfill(10)) : zfill()로 10자리 숫자 만들기
# map, zip, lambda