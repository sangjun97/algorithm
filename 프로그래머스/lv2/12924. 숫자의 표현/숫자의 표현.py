def solution(n):
    answer = 1
    a=[]
    for i in range(n//2):
        while sum(a)<n:
            a.append(i+1)
            i+=1
        if sum(a)==n:
            answer+=1
            a=[]
        else:
            a=[]
    return answer