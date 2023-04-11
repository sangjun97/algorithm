from collections import deque
def solution(priorities, location):
    answer = 0
    priorities = deque(priorities)
    num = deque(list(range(len(priorities))))
    while priorities:
        if max(priorities)<=priorities[0]:
            p = priorities.popleft()
            n = num.popleft()
        else:
            priorities.rotate(-1)
            num.rotate(-1)
            continue
        if n == location:
            answer+=1
            return answer
        else:
            answer+=1
            pass
    return answer