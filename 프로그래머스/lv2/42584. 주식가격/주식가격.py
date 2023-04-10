from collections import deque
def solution(prices):
    answer = []
    prices=deque(prices)
    while prices:
        num=0
        p = prices.popleft()
        for i in prices:
            num+=1
            if i<p:
                break
        answer.append(num)
    return answer