def is_prime(num):
    if num % 2 == 0:
        return False
    
    for i in range(3, int(num ** 0.5) + 1, 2):
        if num % i == 0:
            return False
    
    return True

def dfs(graph, visited, src, selected):
    if visited[src]: return False
    visited[src] = True

    for dst in graph[src]:
        if dst == selected:
            continue

        if slt[dst] == -1 or dfs(graph, visited, slt[dst], selected):
            slt[dst] = src
            return True
    
    return False

N = int(input())
numList = list(map(int, input().split()))

odd_numbers, even_numbers = [], []
for n in numList:
    if n % 2:
        odd_numbers.append(n)
    else:
        even_numbers.append(n)

src_number, dst_number = None, None

first_number = numList[0]
if first_number % 2 == 1:
    src_number, dst_number = odd_numbers, even_numbers
else:
    src_number, dst_number = even_numbers, odd_numbers

src_len, dst_len = len(src_number), len(dst_number)

if src_len != dst_len:
    print(-1)
    exit()

graph = [[] for _ in range(src_len)]

for i in range(src_len):
    for j in range(dst_len):
        if is_prime(src_number[i] + dst_number[j]):
            graph[i].append(j)

answer = []

# 첫번째 수가 dst_number[k]를 선택한 경우에 대해
for k in graph[0]:
    slt = [-1] * dst_len
    slt[k] = 0

    for i in range(1, src_len):
        visited = [False] * src_len
        if not dfs(graph, visited, i, k):
            slt[k] = -1
            break
    
    if slt[k] != -1:
        answer.append(dst_number[k])

if answer:
    print(*sorted(answer))
else:
    print(-1)