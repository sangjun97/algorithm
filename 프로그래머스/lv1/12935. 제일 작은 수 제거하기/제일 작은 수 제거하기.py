def solution(arr):
    answer = []
    arr.pop(arr.index(min(arr)))
    answer=arr
    if arr==[]:
        answer=[-1]
    return answer