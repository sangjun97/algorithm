def solution(cap, n, deliveries, pickups):
    answer = 0
    d=0
    p=0
    for i in reversed(range(n)):
        cnt=0
        d-=deliveries[i]
        p-=pickups[i]
        while d<0 or p<0:
            d+=cap
            p+=cap
            cnt+=1
        answer+=(i+1)*2*cnt
            
            
    return answer