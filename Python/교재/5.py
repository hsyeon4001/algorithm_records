# p161 미로찾기(그래프탐색)
def solve_maze(g, start, end):
    qu = []
    done = set()

    qu.append(start)
    done.add(start)

    while qu:
        p = qu.pop(0)
        v = p[-1]
        if v == end:
            return p
        for x in g[v]:
            if x not in done:
                qu.append(p + x)
                done.add(x)
    
    return '?'

maze = {
    'a': ['e'],
    'b': ['c', 'f'],
    'c': ['b', 'd'],
    'd': ['c'],
    'e': ['a', 'i'],
    'f': ['b', 'g', 'j'],
    'g': ['f', 'h'],
    'h': ['g', 'l'],
    'i': ['e', 'm'],
    'j': ['f', 'k', 'n'],
    'k': ['j', 'o'],
    'l': ['h', 'p'],
    'm': ['i', 'n'],
    'n': ['m', 'j'],
    'o': ['k'],
    'p': ['l']
}

print(solve_maze(maze, 'a', 'p'))

# p168 가짜 동전 찾기1
def weigh(a, b, c, d):
    fake = 14
    if a <= fake and fake <= b:
        return -1
    elif c >= fake and fake <= d:
        return 1
    return 0

def find_fakecoin(left, right):
    for i in range(left+1, right+1):
        result = weigh(left, left, i, i)
        if result == -1:
            return left
        elif result == 1:
            return i
    return '?'
n = 100
print(find_fakecoin(0, n-1))

# p178 가짜 동전 찾기2
def weigh(a, b, c, d):
    fake = 25
    if a <= fake and fake <= b:
        return -1
    elif c <= fake and fake <= d:
        return 1
    return 0

def find_fakecoin(left, right):
    if left == right:
        return left
    
    half = (right - left + 1) // 2
    g1_l = left
    g1_r = left + half - 1
    g2_l = left + half
    g2_r = g2_l + half - 1
    result = weigh(g1_l, g1_r, g2_l, g2_r)

    if result == -1:
        return find_fakecoin(g1_l, g1_r)
    elif result == 1:
        return find_fakecoin(g2_l, g2_r)
    else:
        return right
n = 100
print(find_fakecoin(0, n-1))

# p175 주식 최대수익1
def max_profit(prices):
    n = len(prices)
    max_profit = 0

    for i in range(0, n-1):
        for j in range(i+1, n):
            profit = prices[j] - prices[i]
            if profit > max_profit:
                max_profit = profit
    return max_profit
stock = [10300, 9600, 9800, 8200, 7800, 8300, 9500, 9800, 10200, 9500]
print(max_profit(stock))

# p177 주식 최대수익2
def max_profit(prices):
    n = len(prices)
    min_price = prices[0]
    max_profit = 0

    for i in range(1, n):
        profit = prices[i] - min_price
        if profit > max_profit:
            max_profit = profit
        if prices[i] < min_price:
            min_price = prices[i]
    return max_profit

stock = [10300, 9600, 9800, 8200, 7800, 8300, 9500, 9800, 10200, 9500]
print(max_profit(stock))