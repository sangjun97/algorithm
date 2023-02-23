def solution(left, right):
    answer = 0
    a=[]
    for i in range(left,right+1):
        for j in range(1,int(i**(1/2))+1):
            if i%j==0:
                a.append(j)
                if ( (j**2) != i) : 
                    a.append(i // j)
        if len(a)%2==0:
            answer+=i
        else:
            answer-=i
        a=[]
    return answer
print(solution(1,2))