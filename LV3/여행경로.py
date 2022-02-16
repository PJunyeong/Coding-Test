def solution(tickets):
    nodes = {}
    for tail, head in tickets:
        adjacent = nodes.get(tail, [])
        adjacent.append(head)
        nodes[tail] = adjacent

    for key in nodes.keys():
        nodes[key].sort()

    # ticket의 tail -> head 간선 딕셔너리. 인접 노드는 알파벳 순서대로 정렬

    stack = [["ICN", ["ICN"], list(tickets)]]
    answer = []
    # [현재 노드, 경로, 이 경로에서 사용 가능한 티켓]

    while stack:
        cur_node, path, remaining = stack.pop()

        if not remaining: answer.append(path)
        # 모든 티켓을 사용할 수 있는 경로

        if nodes.get(cur_node):
            for adjacent in nodes.get(cur_node):
                next_path = path + [adjacent]

                if [cur_node, adjacent] not in remaining: continue
                # 현재 남아 있는 티켓에 해당 경로(현재 노드->인접 노드)가 없는 경우

                new_remaining = list(remaining)
                new_remaining.remove([cur_node, adjacent])
                # 사용한 티켓을 제거
                stack.append([adjacent, next_path, new_remaining])

    answer.sort()
    # 가능한 모든 경로를 알파벳 순서대로 정렬
    return answer[0]