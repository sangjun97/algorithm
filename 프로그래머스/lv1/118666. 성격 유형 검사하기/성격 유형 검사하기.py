def solution(survey, choices):
    ans=['R', 'T', 'C', 'F', 'J', 'M', 'A', 'N']
    a=[0,0,0,0,0,0,0,0]
    answer = ''
    
    for i,j in zip(survey, choices):
        if j-4<0:
            a[ans.index(i[0])]+=abs(j-4)
        else:
            a[ans.index(i[1])]+=j-4
    for i in range(4):
        if a[i*2] >= a[i*2+1]:
            answer+=ans[i*2]
        else:
            answer+=ans[i*2+1]
    return answer