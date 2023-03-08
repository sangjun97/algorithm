from string import ascii_lowercase
def solution(s, skip, index):
    answer = ''
    al=ascii_lowercase
    for i in skip:
        al=al.replace(i,'')
    al=list(al)*3
    for i in s:
        answer+=al[al.index(i)+index]
    return answer