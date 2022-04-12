def solution(n, k, cmd):
    answer = ['O'] * n
    linked = [[i-1, i+1] for i in range(n)]
    stack = []

    for command in cmd:
        if command[0] == 'U':
            for _ in range(int(command[2:])):
                k = linked[k][0]
        elif command[0] == 'D':
            for _ in range(int(command[2:])):
                k = linked[k][1]
        elif command[0] == 'C':
            stack.append([k] + linked[k])
            answer[k] = 'X'
            prev_k, next_k = linked[k]
            linked[prev_k][1] = next_k
            if next_k != n:
                linked[next_k][0] = prev_k
                k = next_k
            else:
                k = prev_k
        elif command[0] == 'Z':
            index, prev, next = stack.pop()
            answer[index] = 'O'
            linked[prev][1] = index
            if next != n:
                linked[next][0] = index
    
    return ''.join(answer)

print(solution(8, 2, ["D 2","C","U 3","C","D 4","C","U 2","Z","Z","U 1","C"]))