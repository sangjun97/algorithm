def solution(num, total):
    answer = []
    if total%num==0:
        answer=list(range(total//num-num//2,total//num+num//2+1))
    else:
        answer=list(range(total//num-num//2+1,total//num+num//2+1))
    return answer