def solution(n):
    answer = ''
    num='124'
    def get(n,lists):
        a,b=divmod(n-1,3)
        if b==0:
            lists='1'+lists
        elif b==1:
            lists='2'+lists
        elif b==2:
            lists='4'+lists
        if a==0:
            return lists
        else:
            return get(a,lists)
    answer=''.join(get(n,''))
    return answer

# print('n',solution(13))
# n = 11 result = 42, n = 13 result = 111