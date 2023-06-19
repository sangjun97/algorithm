def solution(n):
    answer = []
    lst=[]
    for i in range(n):
        lst.append(list(range(i+1)))
        
    dir = {0:(1,0), 1:(0,1), 2:(-1,-1)}
    r, c, num = -1,0,1
    for i in range(n):
        for _ in range(i,n):
            dir_r,dir_c = dir[i%3]
            r,c = r+dir_r,c+dir_c
            lst[r][c]=num
            num+=1
    for i in lst:
        answer+=i
    return answer
