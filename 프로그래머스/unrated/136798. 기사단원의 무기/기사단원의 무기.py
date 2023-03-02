def solution(number, limit, power):
    answer = 0
    cnt=0
    for i in range(1,number+1):
        for j in range(1,int(i**0.5)+1):
            if i==j**2:
                cnt+=1
            elif i%j==0:
                cnt+=2
        if cnt>limit:
            answer+=power
        else:
            answer+=cnt
        cnt=0
            
    return answer