def solution(age):
    answer = ''
    abc='abcdefghijklmnopqrstuvwxyz'
    
    for i in str(age):
        answer+=abc[int(i)]
    return answer