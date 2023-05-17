import numpy as np
def check(places):

    a=[]
    for j in range(5):
        for k in range(5):
            if places[j][k]=='P':
                a.append([j,k])    
    for x1,y1 in a:
        for x2,y2 in a:
            dist = abs(x1-x2)+abs(y1-y2)
            if dist==0 or dist>2:
                continue
            elif dist==1:
                return 0
            elif y1==y2 and places[(x1+x2)//2][y1]!='X':
                return 0
            elif x1==x2 and places[x1][(y1+y2)//2]!='X':
                return 0
            elif x1!=x2 and y1!=y2:
                if places[x1][y2]!='X' or places[x2][y1]!='X':
                    return 0
    return 1
                    
def solution(places):
    answer = []
    for i in places:
        answer.append(check(i))
                

    return answer