def solution(citations):
    answer = 0
    citations = sorted(citations, reverse = True)
    for index, i in enumerate(citations):
        if index+1 > i:
            return index
    return index+1