def solution(n):
    answer=[]
    for i in range(1,1000):
        if i%3!=0 and not('3' in str(i)):
            answer.append(i)
            if len(answer)==n:
                answer=answer[-1]
                break
                
    return answer