def solution(spell, dic):
    answer = 2
    for i in dic:
        cnt=0
        for j in spell:
            a=len(i)
            i=i.replace(j,'')
            if len(i)!=a:
                cnt+=1
        if i=="" and cnt==len(spell):
            answer=1
            break
    return answer