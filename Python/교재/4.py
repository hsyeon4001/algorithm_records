# p132 회문찾기(큐, 스택)
def palindrome(s):
    qu = []
    st = []
    
    for x in s:
        if x.isalpha():
            qu.append(x.lower())
            st.append(x.lower())
    
    while qu:
        if qu.pop(0) != st.pop():
            return False
    
    return True

print(palindrome('Wow'))
print(palindrome("Madam, I'm Adam."))
print(palindrome("Madam, I am Adam."))

# p133 연습문제
def solution(s):
    i = 0
    j = len(s)-1
    while i < j:
        if s[i].isalpha() == False:
            i += 1
        elif s[j].isalpha() == False:
            j -= 1
        elif s[i].lower() != s[j].lower():
            return False
        else:
            i += 1
            j -= 1
    return True
print(solution("Madam, I am Adam."))
print(solution("Madam, I'm Adam."))

# p141 동명이인 찾기(딕셔너리)
def find_same_name(a):
    name_dict = dict()
    for name in a:
        if name in name_dict:
            name_dict[name] += 1
        else:
            name_dict[name] = 1
    result = set()
    for name in name_dict:
        if name_dict[name] >= 2:
            result.add(name)
    return result
name = ['Tom', "Jerry", "Mike", "Tom"]
print(find_same_name(name))

# p144 연습문제
def solution(stu, n):
    if n in stu:
        return stu[n]
    else:
        return '?'
stu = {39:'Justin', 14:'John', 67:'Mike', 105:'Summer'}
print(solution(stu, 39))

# p 151 친구찾기(그래프 탐색)
def print_all_friends(g, start):
    qu = []
    done = set()
    qu.append((start, 0))
    done.add(start)
    while qu:
        (a, b) = qu.pop(0)
        print(a, b)
        for x in g[a]:
            if x not in done:
                qu.append((x, b+1))
                done.add(x)
fr_info = {
    'summer': ['john', 'justin', 'mike'],
    'john': ['summer', 'justin'],
    'justin': ['john', 'summer', 'mike', 'may'],
    'mike': ['summer', 'justin'],
    'may': ['justin', 'kim'],
    'kim': ['may'],
    'tom': ['jerry'],
    'jerry': ['tom']
}
print_all_friends(fr_info, 'summer')

# p156 연습문제
def solution(g, x):
    qu = []
    done = set()
    qu.append((1, 0))
    done.add(1)
    while qu:
        (a, b) = qu.pop(0)
        print(a, b)
        if x == a:
            return print('search point:', a, '& distance from start:', b)
        for i in g[a]:
            if i not in done:
                qu.append((i, b+1))
                done.add(i)

sol_dict = {
    1:[2, 3],
    2:[4, 5],
    3:[1],
    4:[2],
    5:[2]
}
solution(sol_dict, 4)