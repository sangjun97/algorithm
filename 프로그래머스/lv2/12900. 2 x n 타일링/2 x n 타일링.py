def solution(n):
    d=[0]*60000
    d[1]=1
    d[2]=2
    d[3]=3
    
    for i in range(3,n+1):
        
        a=d[i-1]+d[i-2]
        d[i]=a%1000000007
        
        
        
    answer = d[n]%1000000007
    return answer