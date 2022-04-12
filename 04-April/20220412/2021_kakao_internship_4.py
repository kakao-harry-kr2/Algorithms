import heapq
INF = 10 ** 9

def solution(n, start, end, roads, traps):
    num_traps = len(traps)
    trap2idx = {traps[i]: i for i in range(num_traps)}
    connection = [[] for _ in range(n+1)]
    outgoings = [{} for _ in range(n+1)]

    for P, Q, S in roads:
        connection[P].append(Q)
        connection[Q].append(P)

        if Q not in outgoings[P].keys():
            outgoings[P][Q] = INF
        outgoings[P][Q] = min(S, outgoings[P][Q])

    distance = [[INF] * (2 ** num_traps) for _ in range(n+1)]
    distance[start][0] = 0

    q = []
    # third element is count(10 bits)
    heapq.heappush(q, [0, start, 0])
    while q:
        dist, now, count = heapq.heappop(q)
        # return answer
        if now == end:
            return dist

        for next in connection[now]:
            bit_now, bit_next = None, None

            if now in traps:
                bit_now = (count >> (num_traps-1-trap2idx[now])) & 1
            if next in traps:
                bit_next = (count >> (num_traps-1-trap2idx[next])) & 1

            flipped = (bit_now if bit_now != None else 0) + (bit_next if bit_next != None else 0)
            if flipped & 1 and now in outgoings[next].keys() and dist + outgoings[next][now] < distance[next][count]:
                distance[next][count] = dist + outgoings[next][now]
                new_count = count
                if bit_next == 0:
                    new_count += 1 << (num_traps-1-trap2idx[next])
                if bit_next == 1:
                    new_count -= 1 << (num_traps-1-trap2idx[next])
                heapq.heappush(q, [dist+outgoings[next][now], next, new_count])
            
            if not flipped & 1 and next in outgoings[now].keys() and dist + outgoings[now][next] < distance[next][count]:
                distance[next][count] = dist + outgoings[now][next]
                new_count = count
                if bit_next == 0:
                    new_count += 1 << (num_traps-1-trap2idx[next])
                if bit_next == 1:
                    new_count -= 1 << (num_traps-1-trap2idx[next])
                heapq.heappush(q, [dist+outgoings[now][next], next, new_count])



print(solution(6, 1, 4, [[1, 2, 1], [2, 5, 1], [5, 6, 1], [6, 3, 1], [3, 2, 1], [3, 4, 1]], [2, 3]))