from collections import Counter
def solution(s):
    answer = []
    s = s.split('},{')
    c=[]
    for i in s:
        a=i.split(',')
        for j in a:
            c.append(int(''.join(list(filter(str.isdigit,j)))))
    q=sorted(Counter(c).items(), key=lambda x: x[1], reverse=True)
    for i in q:
        answer.append(i[0])
    return answer