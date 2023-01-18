import math
def solution(a, b):
    answer = 2
    d=b/math.gcd(a,b)
    while d%2==0:
        d=d//2
    while d%5==0:
        d=d//5
    if d==1:
        answer=1
    return answer