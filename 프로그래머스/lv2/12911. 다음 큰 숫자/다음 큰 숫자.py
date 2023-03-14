def solution(n):
    answer = 0
    i=1
    while 1:
        if bin(n).count('1')==bin(n+i).count('1'):
            return n+i
        i+=1
    return answer