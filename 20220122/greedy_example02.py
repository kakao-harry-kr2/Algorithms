import sys
input = sys.stdin.readline

N, M = map(int, input().split())
table = [list(map(int, input().split())) for _ in range(N)]

smallest_in_list = [min(list) for list in table]

print(max(smallest_in_list))