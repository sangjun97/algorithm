def solution(babbling):
    answer = 0
    a=['aya','ye','woo','ma']
    for i in babbling:
        for j in a:
            if j*2 in i:
                i=i.replace(j*2,'_')
            elif j in i:
                i=i.replace(j,' ')
        if i.replace(' ','')=='':
            answer+=1
    return answer