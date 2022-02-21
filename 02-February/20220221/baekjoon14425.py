# 문자열 집합

import sys
input = sys.stdin.readline

class Node(object):
    def __init__(self, key, count=0):
        self.key = key
        self.child = {}

class Trie(object):
    def __init__(self):
        # 처음 Trie가 만들어지면 빈 Node 하나를 head로 만들어 놓는다.
        self.head = Node(None)

    def insert(self, word):
        cur = self.head

        for ch in word:
            # 해당 문자가 자식노드에 존재하지 않을 경우 노드를 추가
            if ch not in cur.child:
                cur.child[ch] = Node(ch)
            cur = cur.child[ch]
        cur.child['*'] = True

    def search(self, word):
        cur = self.head

        for ch in word:
            if ch not in cur.child:
                return False
            cur = cur.child[ch]
        if '*' in cur.child:
            return True

N, M = map(int, input().split())

trie = Trie()

for _ in range(N):
    word = input().rstrip()
    trie.insert(word)

count = 0
for _ in range(M):
    word = input().rstrip()
    if trie.search(word):
        count += 1

print(count)