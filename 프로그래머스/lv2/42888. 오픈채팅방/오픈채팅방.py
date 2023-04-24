def solution(record):
    answer=[]
    b = []
    a=dict()
    for i in record:
        i= i.split(' ')
        if len(i)==2:
            enter, id = i
        else:
            enter, id, name = i
            a[id]=name
        b.append((enter,id))
    for i in b:
        if i[0]=='Change':
            pass
        elif i[0]=='Enter':
            answer.append("{}님이 들어왔습니다.".format(a[i[1]]))
        elif i[0]=='Leave':
            answer.append("{}님이 나갔습니다.".format(a[i[1]]))
    return answer