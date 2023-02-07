def solution(a, b):
    answer = 0
    if b<a:
        c=a
        a=b
        b=c
    for i in range(a,b+1):
        answer+=i
    return answer