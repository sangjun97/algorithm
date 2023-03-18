def solution(s):
    answer = ''
    a=list(map(int,s.split(' ')))
    answer=str(min(a))+' '+str(max(a))
    return answer