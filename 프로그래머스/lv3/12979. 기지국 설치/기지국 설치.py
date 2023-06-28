from math import ceil
def solution(n, stations, w):
    answer = 0
    W=w*2+1
    start=1
    for i in stations:
        answer+=max(ceil((i-w-start)/W),0)
        start=i+w+1
    if n>=start:
        answer+=ceil((n-start+1)/W)
    return answer

