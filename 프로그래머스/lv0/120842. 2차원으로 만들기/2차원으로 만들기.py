def solution(num_list, n):
    answer = []
    cnt=0
    a=[]
    for i in num_list:
        cnt+=1
        a.append(i)
        if cnt==n:
            cnt=0
            answer.append(a)
            a=[]
        
    
    return answer