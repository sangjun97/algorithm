def solution(numbers, target):
    answer = 0
    overVal = (sum(numbers) - target)//2 
    length = len(numbers)

    def recursive(target, idx, cnt): 
        for i in range(idx, length):
            temp = target
            temp -= numbers[i]
            if temp == 0:
                cnt += 1
            elif temp > 0:
                cnt += recursive(temp, i+1, 0)
            elif temp < 0:
                continue
        return cnt

    return recursive(overVal, 0, 0)