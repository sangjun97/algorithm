from collections import deque
def solution(A, B):
    answer = 0
    
    if max(A) <min(B):
        return len(B)
    elif max(B)<min(A):
        return 0
    
    A = sorted(A,reverse=True)
    B = sorted(B,reverse=True)
    A=deque(A)
    B=deque(B)
    for i in A:
        if i>=B[0]:
            continue
        B.popleft()
        answer+=1
        
    return answer