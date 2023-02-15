def solution(s, n):
    answer = ''
    alpha=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
    for i in range(len(s)):
        if s[i].isupper():
            answer+=alpha[alpha.index(s[i])+n]
        elif s[i]==' ':
            answer+=' '
        else:
            answer+=alpha[alpha.index(s[i].upper())+n].lower()
    return answer