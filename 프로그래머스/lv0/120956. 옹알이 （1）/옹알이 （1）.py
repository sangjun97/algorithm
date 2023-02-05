def solution(babbling):
    answer = 0
    cnt=0
    a=["aya", "ye", "woo", "ma" ]
    for i in babbling:
        for j in a:
            if j in i:
                i=i.replace(j,' ')   
                cnt+=1
        if ' '*cnt==i:
            answer+=1
        cnt=0
    return answer