import sys

def solution(k, room_number):
    sys.setrecursionlimit(10000000)
    rooms = {}

    def find(node):
        if node not in rooms:
            rooms[node] = node + 1
            return node
        else:
            room = find(rooms[node])
            rooms[node] = room + 1
            return room

    results = [find(number) for number in room_number]
    return results
