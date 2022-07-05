import sys
input = sys.stdin.readline

nA, nB = map(int, input().split())

listA = list(map(int, input().split()))
listB = list(map(int, input().split()))

print(len(listA) + len(listB) -  2 * len(list(set(listA).intersection(set(listB)))))