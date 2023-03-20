def solution(s):
    answer = ''
    s=list(s)
    cnt=0
    for i in s:
        if i==' ':
            cnt=0
            answer+=' '
        elif cnt==0:
            answer+=i.upper()
            cnt+=1
        else:
            answer+=i.lower()
            cnt+=1
    return answer