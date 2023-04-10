from collections import deque
import math
def solution(progresses, speeds):
    answer = []
    progresses = deque(progresses)
    speeds = deque(speeds)
    while progresses:
        p = progresses.popleft()
        s = speeds.popleft()
        if answer:
            if math.ceil((100-p)/s) <= num:
                answer[-1]+=1
            else:    
                num = math.ceil((100-p)/s)
                answer.append(1)
        else:    
            num = math.ceil((100-p)/s)
            answer.append(1)
    return answer