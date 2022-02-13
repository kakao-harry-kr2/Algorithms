# Algorithms
Algorithms CT

## 시공간 복잡도

- N < 500 : O(N^3)
- N < 2000 : O(N^2)
- N < 100000 : O(NlogN)
- N < 10000000 : O(N)
- 1000만 단위 이상의 리스트 -> 다른 알고리즘을 생각해보자!

## 생각해볼만한 상황들

- DFS에서 RecursionError : sys.setrecursionlimit(max_depth)
- 문제에 제시된 수들의 범위에 주목하자! : 메모리초과 & 시간초과 & 예외처리
- 반복되는 계산은 리스트를 통해 저장해놓고 사용하자!

## 유형별 생각해볼만한 문제들

- Dynamic programming : 7579, 11066, 14002(LIS), 2533(+tree)
- Graph : 9370, 10217(+dp), 11657(BellmanFord)
- Meet in the Middle : 1450(Binary Search)