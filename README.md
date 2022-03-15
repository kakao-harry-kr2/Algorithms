# Algorithms
Algorithms CT

## 시공간 복잡도

- Time Complexity : 10 ^ 7 CNT/s

## 생각해볼만한 상황들

- DFS에서 RecursionError : sys.setrecursionlimit(max_depth)
- 문제에 제시된 수들의 범위에 주목하자! : 메모리초과 & 시간초과 & 예외처리
- 반복되는 계산은 리스트를 통해 저장해놓고 사용하자!

## ALGORITHMS

- Dijkstra : fixed start & NOT negative weight
- BellmanFord : fixed start & negative weights & NOT negative cycle
- FloydWarshall : arbitrary start/end & negative weights & NOT negative cycle
- Kosaraju : find Strongly Connected Component

## 유형별 생각해볼만한 문제들

- Dynamic programming : 1086(1D+bitmask), 1509, 2169, 1648(2D+bitmask), 11003, 5977(+deque)
- Graph : 10217(+dp), 11280(2-SAT-3), 11281(2-SAT-4)
- Meet in the Middle : 1450(Binary Search)
- String : 1786(KMP)
- Segment Tree : 2042, 16975(lazy), 5419, 7626