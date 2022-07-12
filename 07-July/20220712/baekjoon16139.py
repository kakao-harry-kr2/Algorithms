import sys
input = sys.stdin.readline

S = input().rstrip()
q = int(input())

# table[i][j]: i번째 알파벳이 문자열에서 j번째에 나타나는지?
table = [[0] * (len(S)+1) for _ in range(26)]
for index, c in enumerate(S):
    table[ord(c)-97][index] = 1

# table[i][j]: i번째 알파벳이 문자열에서 j번째까지 몇개가 나타나는지?
for i in range(26):
    for j in range(len(S)-1):
        table[i][j+1] += table[i][j]

for _ in range(q):
    alphabet, l, r = input().split()
    print(table[ord(alphabet)-97][int(r)] - table[ord(alphabet)-97][int(l)-1])