from heapq import heappop, heappush, heapify
def solution(scoville, K):
    answer = 0
    heapify(scoville)
    if scoville[0] >= K:
        return answer
    while scoville:      
        if len(scoville) == 1 and scoville[0] <= K:
            return -1
        elif scoville[0]< K:
            s = heappop(scoville)
            v = heappop(scoville)
            heappush(scoville,v*2+s)
            answer+=1
        else:
            return answer
    return answer