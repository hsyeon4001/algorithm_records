# p80 3-7-1 순차탐색
def search_list(arr, x):
    n = len(arr)
    for i in range(0, n):
        if arr[i] == x:
            return i

    return -1
v = [17, 92, 18, 33, 58, 7, 33, 42]
print(search_list(v, 18))
print(search_list(v, 7))
print(search_list(v, 300))

# p83 3-7 연습문제
def search_list(arr, x):
    answer = []
    n = len(arr)
    for i in range(0, n):
        if arr[i] == x:
            answer.append(i)
    return answer
v = [17, 92, 18, 33, 58, 7, 33, 42]
print(search_list(v, 18))
print(search_list(v, 33))
print(search_list(v, 300))

def search_stu(stu_no, x):
    n = len(stu_no)
    for i in range(0, n):
        if stu_no[i] == x:
            return stu_name[i]
    return '?'

stu_no = [39, 14, 67, 105]
stu_name = ['Justin', 'John', 'Mike', 'Summer']
print(search_stu(stu_no, 14))
print(search_stu(stu_no, 54))

# p86 3-8-2 선택정렬1
def find_min_i(arr):
    n = len(arr)
    min_i = 0
    for i in range(1, n):
        if arr[i] < arr[min_i]:
            min_i = i
    return min_i

def sel_sort(arr):
    n = len(arr)
    answer = []
    while arr:
        for i in range(0, n):
            min_i = find_min_i(arr)
            min_v = arr.pop(min_i)
            answer.append(min_v)
    return answer

d = [2, 4, 5, 1, 3]
print(sel_sort(d))

# p89 선택정렬2
def sel_sort(arr):
    n = len(arr)
    for i in range(0, n-1):
        min_i = i
        for j in range(i+1, n):
            if arr[j] < arr[min_i]:
                min_i = j
            arr[i], arr[min_i] = arr[min_i], arr[i]
    return arr
d = [4, 5, 9, 32, 1, 65]
print(sel_sort(d))

# p91 연습문제
def sel_sort(arr):
    n = len(arr)
    for i in range(0, n-1):
        max_i = i
        for j in range(i+1, n):
            if arr[j] > arr[max_i]:
                max_i = j
            arr[i], arr[max_i] = arr[max_i], arr[i]
    return arr
print(sel_sort([2, 4, 5, 1, 3]))

# p93 삽입정렬1
def find_ins_idx(arr, v):
    for i in range(0, len(arr)):
        if arr[i] > v:
            return i
    return len(arr)

def ins_sort(arr):
    result = []
    while arr:
        ele = arr.pop(0)
        idx = find_ins_idx(result, ele)
        result.insert(idx, ele)
    return result

print(ins_sort([2, 4, 5, 1, 3]))


# p96 삽입정렬2
def ins_sort(arr):
    n = len(arr)
    for i in range(1, n):
        key = arr[i]
        j = i-1
        while j >= 0 and arr[j] > key:
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = key
    return arr
print(ins_sort([2,4,5,1,3]))

# p98 연습문제
def ins_sort(arr):
    n = len(arr)
    for i in range(1, n):
        j = i-1
        key = arr[i]
        while j >= 0 and arr[j] < key:
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = key
    return arr
print(ins_sort([2,4,5,1,3]))

# p100 병합정렬
def merge_sort(a):
    n = len(a)
    if n <= 1:
        return
    mid = n // 2
    g1 = a[:mid]
    g2 = a[mid:]
    merge_sort(g1)
    merge_sort(g2)

    i1 = 0
    i2 = 0
    ia = 0
    while i1 < len(g1) and i2 < len(g2):
        if g1[i1] < g2[i2]:
            a[ia] = g1[i1]
            i1 += 1
            ia += 1
        else:
            a[ia] = g2[i2]
            i2 += 1
            ia += 1

    while i1 < len(g1):
        a[ia] = g1[i1]
        i1 += 1
        ia += 1
    while i2 < len(g2):
        a[ia] = g2[i2]
        i2 += 1
        ia += 1
    
d = [6, 8, 3, 9, 10, 1, 2, 4, 7, 5]
merge_sort(d)
print(d)

# P107 연습문제
def merge_sort(a):
    n = len(a)
    if n <= 1:
        return
    
    mid = n // 2
    g1 = a[:mid]
    g2 = a[mid:]
    merge_sort(g1)
    merge_sort(g2)

    i1, i2, ia = 0, 0, 0
    while i1 < len(g1) and i2 < len(g2):
        if g1[i1] > g2[i2]:
            a[ia] = g1[i1]
            i1 += 1
            ia += 1
        else:
            a[ia] = g2[i2]
            i2 += 1
            ia += 1
    
    while i1 < len(g1):
        a[ia] = g1[i1]
        i1 += 1
        ia += 1
    while i2 < len(g2):
        a[ia] = g2[i2]
        i2 += 1
        ia += 1
d = [6, 8, 3, 9, 10, 1, 2, 4, 7, 5]
merge_sort(d)
print(d)

# p110 퀵정렬
def quick_sort(a):
    n = len(a)
    if n <= 1:
        return a

    pivot = a[-1]
    g1 = []
    g2 = []

    for i in range(0, n-1):
        if a[i] < pivot:
            g1.append(a[i])
        else:
            g2.append(a[i])
    
    return quick_sort(g1) + [pivot] + quick_sort(g2)

d = [6, 8, 3, 9, 10, 1, 2, 4, 7, 5]
print(quick_sort(d))

# p115 연습문제(버블정렬)
def bubble_sort(a):
    n = len(a)
    chk = False
    for i in range(0, n-1):
        for j in range(i+1, n):
            if a[i] > a[j]:
                a[i], a[j] = a[j], a[i]
    return a
d = [6, 8, 3, 9, 10, 1, 2, 4, 7, 5]
bubble_sort(d)
print(d)

# p123 이분탐색
def binary_search(a, x):
    start = 0
    end = len(a)-1

    while start <= end:
        mid = (start + end) // 2
        if x == a[mid]:
            return mid
        elif x > a[mid]:
            start = mid + 1
        else:
            end = mid - 1
    return -1
d = [1,4,9,16,25,36,49,64,81]
print(binary_search(d, 36))

# p125 연습문제(미해결)
def binary_search(a, x):
    start = 0
    end = len(a)-1
    if len(a) == 0:
        return -1

    mid = (start + end) // 2
    print(mid)
    if x == a[mid]:
        
    elif x > a[mid]:
        start = mid + 1
        binary_search(a[start:], x)
    else:
        end = mid - 1
        binary_search(a[:end], x)

d = [1,4,9,16,25,36,49,64,81]
print(binary_search(d, 36))

