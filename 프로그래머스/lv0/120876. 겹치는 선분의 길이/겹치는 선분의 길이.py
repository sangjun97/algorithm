from collections import Counter
def solution(lines):
    answer = 0
    a=[]
    for i in lines:
        a+=(list(range(i[0],i[1])))
    result=Counter(a)
    for key in result:
        if result[key]>2:
            answer-=1
    answer+=len(a)-len(set(a))
    return answer
