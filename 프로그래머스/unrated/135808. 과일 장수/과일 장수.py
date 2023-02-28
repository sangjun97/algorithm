from collections import Counter
def solution(k, m, score):
    answer = 0
    score=sorted(score,reverse=True)
    for i in range(len(score)//m):
        a=score[i*m:m*(i+1)]
        answer+=len(a)*a[-1]
    return answer