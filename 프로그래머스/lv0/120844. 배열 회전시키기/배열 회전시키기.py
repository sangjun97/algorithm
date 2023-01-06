def solution(numbers, direction):
    answer=[]
    if direction=='right':
        numbers.insert(0,numbers[-1])
        numbers.pop(-1)
        answer=numbers
    else:
        numbers.append(numbers[0])
        print(numbers)
        numbers.pop(0)
        answer=numbers
        
    return answer