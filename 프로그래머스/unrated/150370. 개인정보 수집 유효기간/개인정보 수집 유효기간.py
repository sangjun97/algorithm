def solution(today, terms, privacies):
    answer = []
    term=dict()
    today=today.split('.')
    today=int(today[2])+int(today[1])*28+int(today[0])*12*28
    cnt=0
    for i in terms:
        term[i.split()[0]]=int(i.split()[1])
    for i in privacies:
        cnt+=1
        i=i.split()
        j=i[0].split('.')
        day=int(j[2])+int(j[1])*28+int(j[0])*12*28+term[i[1]]*28
        if day<today+1:
            answer.append(cnt)
    return answer