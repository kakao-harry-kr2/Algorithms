N = int(input())
info = [list(map(int, input().split())) for _ in range(N)]

x_list = sorted([x for x, _, _ in info])
y_list = sorted([y for _, y, _ in info])

needs = 2 * (max(x_list) - min(x_list) + max(y_list) - min(y_list))

count = 0
while needs > 0:
    diff = [0] * (N - count)
    for i, (x, y, c) in enumerate(info):
        diff[i] += c

        x_idx = x_list.index(x)
        if x_idx == 0:
            diff[i] += 2 * (x_list[1] - x_list[0])
        elif x_idx == N - 1 - count:
            diff[i] += 2 * (x_list[-1] - x_list[-2])

        y_idx = y_list.index(y)
        if y_idx == 0:
            diff[i] += 2 * (y_list[1] - y_list[0])
        elif y_idx == N - 1 - count:
            diff[i] += 2 * (y_list[-1] - y_list[-2])

    max_diff, max_idx = 0, -1
    for i in range(N - count):
        if diff[i] > max_diff:
            max_diff = diff[i]
            max_idx = i

    print(max_diff, info[max_idx])

    x_list.remove(info[max_idx][0])
    y_list.remove(info[max_idx][1])
    info.remove(info[max_idx])

    count += 1
    needs -= max_diff

print(count)