import numpy as np
def solution(arr):
    answer = [0,0]
    def loop(arr):
        a=[]
        n = len(arr)//2
        a.append(np.split(arr,(n,n),axis=1)[0][:n])
        a.append(np.split(arr,(n,n),axis=1)[0][n:])
        a.append(np.split(arr,(n,n),axis=1)[2][:n])
        a.append(np.split(arr,(n,n),axis=1)[2][n:])
        for i in a:
            if len(np.unique(i))==2:
                loop(i)
            else:
                answer[np.unique(i)[0]]+=1
    arr = np.array(arr)
    if len(np.unique(arr))==2:
        loop(arr)
    else:
        answer[np.unique(arr)[0]]+=1
    return answer