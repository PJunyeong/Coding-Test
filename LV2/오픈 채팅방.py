def solution(record):
    result = []
    id_name = {}

    for rec in record:
        rec = rec.split()
        # move / id / nickname 분류
        move = rec[0]
        user_id = rec[1]
        result.append([user_id, move])
        # id별 move를 순서대로 파악

        if move == 'Enter' or move == 'Change':
            id_name[user_id] = rec[2]
            # 채팅방 nickname 바뀌는 순간은 Enter(다른 nickname으로 들어올 때) 또는 Change

    answer = []

    for rec in result:
        if rec[1] == 'Enter':
            answer.append(id_name.get(rec[0]) + '님이 들어왔습니다.')
        elif rec[1] == 'Leave':
            answer.append(id_name.get(rec[0]) + '님이 나갔습니다.')
        # 기록된 순서에 따라 id별 move를 기록. nickname은 마지막으로 설정된 nickname 사용

    return (answer)