def solution(sides):
    answer = 0
    a=sorted(sides)[-1]
    b=sorted(sides)[0]
    answer=2*b-1
    return answer