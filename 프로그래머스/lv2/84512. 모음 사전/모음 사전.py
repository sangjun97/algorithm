def solution(word):
    answer = len(word)
    num = ['A','E','I','O','U']
    a=781
    for i in range(len(word)):
        answer+=num.index(word[i])*a
        a=(a-1)//5
    
    return answer