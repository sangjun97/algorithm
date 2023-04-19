def solution(brown, yellow):
    answer = []
    n = int(yellow**0.5)
    x = 0
    for i in reversed(range(1,n+1)):
        if yellow%i==0:
            x = i + 2
            y = yellow//i + 2
            if x*y-yellow==brown:
                break
    if not x:
        x = 1
        y = yellow
    answer = [max(x,y),min((x,y))]
    return answer