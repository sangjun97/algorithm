def solution(numbers):
    answer = ''
    answer=''.join(sorted(list(map(str,numbers)), key = lambda x : (x * 4)[:4], reverse = True))
    if answer[0]=='0':
        return '0'
    return answer