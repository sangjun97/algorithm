def solution(n):
    answer = 0
    a=1
    for i in range(n):
        if n%a==1:
            break
        else:
            a+=1
    return a