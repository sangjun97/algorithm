def solution(a, b):
    answer = ''
    day=['SUN','MON','TUE','WED','THU','FRI','SAT']
    month=[31,29,31,30,31,30,31,31,30,31,30,31]
    answer=day[(sum(month[:a-1])+b+4)%7]
    return answer