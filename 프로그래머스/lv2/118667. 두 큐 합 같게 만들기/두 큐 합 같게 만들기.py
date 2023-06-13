from collections import deque
def solution(queue1, queue2):
    queue1=deque(queue1)
    queue2=deque(queue2)
    q1 = sum(queue1)
    q2 = sum(queue2)
    limit=len(queue1)+len(queue2)
    cnt=0
    while q1!=q2:
        if cnt>limit+5:
            return -1
        if q1 and q1>q2:
            tmp = queue1.popleft()
            queue2.append(tmp)
            q1-=tmp
            q2+=tmp
            cnt+=1
        elif q2 and q1<q2:
            tmp = queue2.popleft()
            queue1.append(tmp)
            q1+=tmp
            q2-=tmp
            cnt+=1   
            
    return cnt