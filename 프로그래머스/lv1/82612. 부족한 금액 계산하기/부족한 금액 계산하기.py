def solution(price, money, count):
    answer = -1
    a=0
    for i in range(1,count+1):
        a+=i
    answer=money-price*a
    if answer>=0:
        answer=0

    return abs(answer)