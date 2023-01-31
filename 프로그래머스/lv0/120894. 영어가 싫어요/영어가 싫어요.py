def solution(numbers):
    answer = ''
    num=["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    a=''
    for i in numbers:
        a+=i
        if a in num:
            answer+=str(num.index(a))
            a=''
    return int(answer)