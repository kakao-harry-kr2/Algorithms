def solution(record):
    uid2nick = dict()
    logs = []
    for rec in record:
        rec_splitted = rec.split()
        if rec_splitted[0] == 'Enter':
            uid, nickname = rec_splitted[1:]
            uid2nick[uid] = nickname
            logs.append((uid, True))
        elif rec_splitted[0] == 'Leave':
            uid = rec_splitted[1]
            logs.append((uid, False))
        else:
            uid, nickname = rec_splitted[1:]
            uid2nick[uid] = nickname

    answer = []
    for uid, enter in logs:
        if enter:
            answer.append(uid2nick[uid]+"님이 들어왔습니다.")
        else:
            answer.append(uid2nick[uid]+"님이 나갔습니다.")

    return answer