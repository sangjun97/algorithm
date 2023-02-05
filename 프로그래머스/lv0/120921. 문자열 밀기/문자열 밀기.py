def solution(A, B):
    answer = 0
    for i in range(len(A)):
        if A==B:
            break
        elif A[-1]+A[:-1]!=B:
            A=A[-1]+A[:-1]
            answer+=1
        else:
            answer+=1
            break
    if answer>=len(A):
        answer=-1
    return answer