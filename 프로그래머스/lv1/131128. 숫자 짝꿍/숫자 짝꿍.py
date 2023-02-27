from collections import Counter
def solution(X, Y):
    answer = ''
    for i in list(Counter(X).items()):
        for j in list(Counter(Y).items()):
            if i[0]==j[0]:
                answer+=i[0]*min(int(i[1]),int(j[1]))
                break
    if answer=='':
        return '-1'
    elif answer[0]=='0':
        return '0'
    return ''.join(sorted(answer,reverse=True))