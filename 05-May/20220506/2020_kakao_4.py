class Node(object):
    def __init__(self, key, count=0):
        self.key = key
        self.count = count
        self.child = {}

class Trie(object):
    def __init__(self):
        # 처음 Trie가 만들어지면 빈 Node 하나를 head로 만들어 놓는다.
        self.head = Node(None)

    def insert(self, word):
        cur = self.head
        cur.count += 1
        
        for ch in word:
            # 해당 문자가 자식노드에 존재하지 않을 경우 노드를 추가
            if ch not in cur.child:
                cur.child[ch] = Node(ch)
            cur = cur.child[ch]
            cur.count += 1

    def search(self, word):
        cur = self.head

        for ch in word:
            if ch not in cur.child:
                return 0
            cur = cur.child[ch]
        
        return cur.count

def solution(words, queries):
    tries1 = [Trie() for _ in range(10001)]
    tries2 = [Trie() for _ in range(10001)]
    for word in words:
        tries1[len(word)].insert(word)
        tries2[len(word)].insert(word[::-1])
    
    answer = [0] * len(queries)
    for idx, query in enumerate(queries):
        if query[-1] == '?':
            answer[idx] = tries1[len(query)].search(query.replace('?', ''))
        else:
            answer[idx] = tries2[len(query)].search(query[::-1].replace('?', ''))
    
    return answer

print(solution(["frodo", "front", "frost", "frozen", "frame", "kakao"], ["fro??", "????o", "fr???", "fro???", "pro?"]))