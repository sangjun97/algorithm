def solution(arr):
    answer = 0
    a=1
    for i in range(0,len(arr)):
        for j in range(max(arr[i],a), (arr[i]*a)+1):
            if j%arr[i]==0 and j%a==0:
                a=j
                break
    return a