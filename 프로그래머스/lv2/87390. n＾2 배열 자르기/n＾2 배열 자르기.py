def solution(n, left, right):
    answer = []
    for i in range(left,right+1):
        r=i%n
        c=i//n
        answer.append(max(r,c)+1)
    return answer