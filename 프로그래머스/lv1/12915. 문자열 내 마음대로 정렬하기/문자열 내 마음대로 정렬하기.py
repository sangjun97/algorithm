def solution(strings, n):
    answer = []
    a=[]
    for i in strings:
        a.append(i[n]+i)
    a=sorted(a)
    for i in a:
        answer.append(i[1:])
        
    return answer