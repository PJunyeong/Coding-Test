# 1. 힙으로 풀기
import heapq
def solution(jobs):
    jobs.sort()
    # 요청 시간 기준 정렬
    total = 0
    jobs_num = len(jobs)
    cur_time = jobs[0][0]
    heap = []

    while jobs:
        req, taken = jobs.pop(0)
        cur_time += taken
        total += cur_time - req
        # 요청된 job은 곧바로 처리 가능
        # 현재 시간: += 소요 시간, 전체 처리 시간: += (현재 시간 - 요청 시간)

        while jobs and jobs[0][0] < cur_time:
            req, taken = jobs.pop(0)
            heapq.heappush(heap, [-taken, req])
        while heap:
            taken, req = heapq.heappop(heap)
            jobs.insert(0, [req, -taken])
            # 현재 작업 중인 job 이외에 cur_time까지 요청 들어온 job을 소요 시간에 따라 정렬

    return total // jobs_num

# 2. 리스트로 풀기
# def solution(jobs):
#     jobs.sort()
#     # 요청 시간 기준 정렬
#     total = 0
#     jobs_num = len(jobs)
#     cur_time = jobs[0][0]
#     tmp = []
#     while jobs:
#         req, taken = jobs.pop(0)
#         cur_time += taken
#         total += cur_time - req
#         # 요청된 job은 곧바로 처리 가능
#         # 현재 시간: += 소요 시간, 전체 처리 시간: += (현재 시간 - 요청 시간)
#
#         while jobs and jobs[0][0] < cur_time:
#             tmp.append(jobs.pop(0))
#
#         tmp.sort(key=lambda x:x[1])
#         jobs = tmp + jobs
#         tmp = []
#             # 현재 작업 중인 job 이외에 cur_time까지 요청 들어온 job을 소요 시간에 따라 정렬
#
#     return total // jobs_num