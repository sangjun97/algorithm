def solution(sides):
    answer = 2
    sides=sorted(sides)
    if sides[0]+sides[1]>sides[2]:
        answer=1
    return answer