from collections import Counter
def solution(N, stages):
    answer = []
    a={}
    tmp=[]
    length=len(stages)
    for i in range(1,N+1):   
        if length!=0:
            a[i]=stages.count(i)/length
            length-=stages.count(i)
        else:
            a[i]=0
    answer=sorted(a,key=lambda key: a[key],reverse=True)

    return answer