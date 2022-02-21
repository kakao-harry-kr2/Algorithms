# 휴대폰 자판

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
        self.num_of_typing = 0

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

    def count(self, cur:Node, typing):
        keys = sorted(cur.child.keys())

        if cur != self.head and len(keys) == 1:
            if keys[0] == '*':
                self.num_of_typing += typing
                return
            self.count(cur.child[keys[0]], typing)
            return
        
        for key in keys:
            if key == '*':
                self.num_of_typing += typing
            else:
                self.count(cur.child[key], typing+1)

while True:
    try:
        N = int(input())
    except:
        break

    trie = Trie()
    for _ in range(N):
        word = input().rstrip()
        trie.insert(word)
    
    trie.count(trie.head, 0)

    print("%.2f" % (trie.num_of_typing / N))