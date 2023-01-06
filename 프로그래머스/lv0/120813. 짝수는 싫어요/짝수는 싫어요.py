def solution(n):
    answer=[]
    for i,num in enumerate(range(n)):
        if n<i*2+1:
            return answer
        else:
            answer.append(i*2+1)
        
    return answer