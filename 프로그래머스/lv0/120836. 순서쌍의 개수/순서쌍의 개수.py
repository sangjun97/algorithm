def solution(n):
    answer=0
    for i in range(1,1000001):
        if n%i==0:
            answer+=1
    return answer