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
