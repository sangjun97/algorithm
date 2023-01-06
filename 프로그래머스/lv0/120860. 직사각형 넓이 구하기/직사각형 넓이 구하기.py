def solution(dots):
    answer = 0
    dots=sorted(dots)
    answer=abs((dots[0][0]-dots[2][0])*(dots[0][1]-dots[3][1]))
    return answer