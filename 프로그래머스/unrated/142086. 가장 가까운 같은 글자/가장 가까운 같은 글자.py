import numpy as np
def solution(s):
    answer = []
    a=[]
    for i in s:
        if i not in a:
            a.append(i)
            answer.append(-1)
        else:
            a.append(i)
            num=np.where(np.array(a)==i)[0]
            answer.append(int(num[-1])-int(num[-2]))
    return answer