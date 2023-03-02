def solution(k, score):
    answer = []
    a=[]
    for i in score:
        a.append(i)
        a=sorted(a,reverse=True)
        if len(a)>k:
            a.pop()
        answer.append(min(a))
    return answer