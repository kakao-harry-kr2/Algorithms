f_input = open('/Users/mini/Downloads/Problems_Complete_ACM_2004/b.in', 'r')
input = f_input.readline
f_output = open('/Users/mini/Downloads/Problems_Complete_ACM_2004/b1.out', 'w')

import sys
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    N = int(input())

    parent = [-1] * (N+1)
    dist = [0] * (N+1)

    while True:
        command = input().split()

        if command[0] == 'O':
            break

        if command[0] == 'E':
            i = int(command[1])
            selected_i = i

            stack = []
            while parent[i] != -1:
                stack.append(i)
                i = parent[i]

            while stack:
                now = stack.pop()
                dist[now] += dist[parent[now]]
                parent[now] = i
            
            print(dist[selected_i])
            # f_output.write(str(dist[selected_i]) + '\r\n')
        
        if command[0] == 'I':
            i, j = int(command[1]), int(command[2])
            parent[i] = j
            dist[i] = abs(i-j) % 1000

f_input.close()
f_output.close()