# Q1.
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

ord(): 문자 -> 숫자
chr(): 숫자 -> 문자 
list comprehension : [i(실행문) for i in range(10)] 간결한 코드로 리스트 생성 가능
print([f'{i} X {j} = {i*j}' for i in range(2, 10) for j in range(1, 10)]) : list comprehension 사용한 구구단
zfill(): 자리수 맞추기
print('111'.zfill(10)) : zfill()로 10자리 숫자 만들기
map, zip, lambda

# Q2.
def survival(durabilities, dogs):
    survivor = [ i['이름'] for i in dogs ]
    for i in dogs:
        location = 0
        while location < len(durabilities)-1:
            location += int(i['점프력'])
            durabilities[location-1] -= int(i['몸무게'])
            if durabilities[location-1] < 0:
                del survivor[survivor.index(i['이름'])]
                break
    return survivor

durabilities = [1, 2, 1, 4]
dogs = [{
    "이름" : "루비독",
    "나이" : "95년생",
    "점프력" : "3",
    "몸무게" : "4",
    },{
    "이름" : "피치독",
    "나이" : "95년생",
    "점프력" : "3",
    "몸무게" : "3",
    },{
    "이름" : "씨-독",
    "나이" : "72년생",
    "점프력" : "2",
    "몸무게" : "1",
    },{
    "이름" : "코볼독",
    "나이" : "59년생",
    "점프력" : "1",
    "몸무게" : "1",
    },
]

print(survival(durabilities.copy(), dogs.copy()))

# Q3.
import datetime
def solution(waiting):
    boarding = [25, 15, 15, 15, 15, 15]
    wait_d, wait_p = divmod(waiting, 1200)
    months = [ 2 ** i for i in range(10, 0, -1) ]
    year, remain_d = divmod(wait_d, sum(months))
    m_index = 0
    for i in months:
        if i <= remain_d:
            remain_d -= i
            m_index += 1
        else:
            break
    month = m_index + 1
    day = remain_d + 1
    add_h, remain_p = divmod(wait_p, sum(boarding))
    d = datetime.datetime.today()
    hour = d.hour + add_h
    b_index = d.minute // 10
    for i in boarding:
        if i <= remain_p:
            remain_p -= i
            b_index += 1
        else:
            break
    minutes = (b_index + 1) * 10
    if b_index == len(boarding) - 1:
        hour += 1
        minutes -= 60
    print(f'{2020+year}년 {month}월 {day}일 {hour}시 {minutes}분 출발')

# Q4.
def solution(pages):
    answer = 0
    chair = []
    
    for i in pages:
        if len(chair) < 3:
            if i in chair:
                chair.remove(i)
                chair.append(i)
                answer += 1
            else:
                chair.append(i)
                answer += 60
        else:
            if i in chair:
                chair.remove(i)
                chair.append(i)
                answer += 1
            else:
                chair.pop(0)
                chair.append(i)
                answer += 60

    return f'{answer // 60}분 {answer % 60}초'
pages = ['척추동물', '어류', '척추동물', '무척추동물', '파충류', '척추동물', '어류', '파충류']
print(solution(pages))

# Q5.
def solution(graph, start):
    stack = [start]
    visited = []

    while stack:
        x = stack.pop()
        visited.append(x)
        nodes = graph[x] - set(visited)
        if len(nodes) == 0:
            break
        stack.append(min(nodes))

graph = {100: set([67, 66]),
        67: set([100, 82, 63]),
        66: set([100, 73, 69]),
        82: set([67, 61, 79]),
        63: set([67]),
        73: set([66]),
        69: set([66, 65, 81]),
        61: set([82]),
        79: set([82, 87, 77]),
        65: set([69, 84, 99]),
        81: set([69]),
        87: set([79, 31, 78]),
        77: set([79]),
        84: set([65]),
        99: set([65]),
        31: set([87]),
        78: set([87])}
solution(graph, 100)

# Q6. 
import numpy as np
def solution(field1, field2):
    field3 = np.rot90(field2, 1) + np.array(field1)
    print(field3)
    for i in field3:
        print(chr(int((''.join(str(i))[1:-1].replace(' ', '')), 8)))
f1 = [
    [1,0,0,0,0],
    [0,0,1,0,1],
    [0,0,1,0,1],
    [0,0,1,0,1],
    [0,0,1,0,1]
]
f2 = [
    [0,0,0,0,1],
    [0,0,0,0,3],
    [0,0,0,0,4],
    [0,2,0,0,2],
    [4,5,0,2,0]
]
solution(f1, f2)