def solution(emergency):
    a = sorted(emergency)
    answer=[]
    for i in a:
        for j in range(len(emergency)):
            if emergency[j]==i:
                answer.append(abs(j+1-len(emergency))+1)
            
    return answer