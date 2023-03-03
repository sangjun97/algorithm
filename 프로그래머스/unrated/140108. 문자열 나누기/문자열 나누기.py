def solution(s):
    answer = 0
    x=0
    y=0
    ans=''
    for i in s:
        if x==0:
            ans=i
            x+=1
        elif ans==i:
            x+=1
        elif ans!=i:
            y+=1
        if x==y:
            answer+=1
            x=0
            y=0
    if x!=0:
        answer+=1     
    return answer