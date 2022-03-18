def name2num(name):
    return (ord(name[0])-65) * 26 ** 2 + (ord(name[1])-65) * 26 + ord(name[2])-65

def num2name(num):
    return chr(num // (26 ** 2) + 65) + chr((num // 26) % 26 + 65) + chr(num % 26 + 65)

def dfs(start, graph, history:list, T):
    history.append(start)
    if len(history) == T:
        return True
    
    for i in range(len(graph[start])):
        if not graph[start][i][1]:
            graph[start][i][1] = True
            if dfs(graph[start][i][0], graph, history, T):
                return True
            graph[start][i][1] = False
            history.pop()
    
    return False

def solution(tickets):
    graph = [[] for _ in range(26**3)]
    for a, b in tickets:
        A = name2num(a)
        B = name2num(b)
        graph[A].append([B, False])

    for i in range(26**3):
        graph[i].sort()
    
    now = name2num("ICN")
    
    history = []

    T = len(tickets) + 1
    
    dfs(now, graph, history, T)
    
    answer = []
    for h in history:
        answer.append(num2name(h))

    return answer

print(solution([["ICN", "ABC"], ["ICN", "BBB"], ["BBB", "ICN"]]))