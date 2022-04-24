N, K = map(int, input().split())
n = 2*N
durability = list(map(int, input().split()))
robot = [False] * n

count = 0
up, down = 0, N-1
while True:
    """ step 1 """
    count += 1
    up = up - 1 if up != 0 else n-1
    down = down - 1 if down != 0 else n-1
    robot[down] = False

    """ step 2 """
    for i in reversed(range(up, down if up < down else n + down)):
        if robot[i%n] and not robot[(i+1)%n] and durability[(i+1)%n]:
            durability[(i+1)%n] -= 1
            robot[(i+1)%n] = True
            robot[i%n] = False

    robot[down] = False
    
    """ step 3 """
    if durability[up]:
        durability[up] -= 1
        robot[up] = True

    """ step 4 """
    if durability.count(0) >= K:
        break

print(count)