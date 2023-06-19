def solution(dirs):
    dic = {'U':(-1,0),'D':(1,0),'L':(0,-1),'R':(0,1)}
    r,c=0,0
    answer=[]
    for i in dirs:
        dir_r,dir_c=dic[i]
        if r+dir_r<-5 or r+dir_r>5 or c+dir_c<-5 or c+dir_c>5:
            continue
        else:
            r2,c2=r+dir_r,c+dir_c
        if (r,c,r2,c2) not in answer or (r2,c2,r,c) not in answer:
            answer.append((r,c,r2,c2))
            answer.append((r2,c2,r,c))
        r=r2
        c=c2
    return len(answer)//2