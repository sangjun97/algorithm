def solution(keyinput, board):
    answer = []
    p=[0,0]
    for i in keyinput:
        if i=="left":
            if p[0]-1<=-(board[0]//2):
                p[0]=-(board[0]//2)
            else:
                p[0]-=1
        elif i=="right":
            if p[0]+1>=(board[0]//2):
                p[0]=(board[0]//2)
            else:
                p[0]+=1
        elif i=="up":
            if p[1]+1>=(board[1]//2):
                p[1]=(board[1]//2)
            else:
                p[1]+=1
        else:
            if p[1]-1<=-(board[1]//2):
                p[1]=-(board[1]//2)
            else:
                p[1]-=1
    return p