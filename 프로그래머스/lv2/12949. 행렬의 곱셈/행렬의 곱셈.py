def solution(arr1, arr2):
    b = len(arr1)
    a = len(arr2[0])

    answer = [[0 for col in range(a)] for row in range(b)]
    for i in range(len(arr1)):
        b=[]
        for j in range(len(arr2[0])):
            a=0
            for k in range(len(arr2)):
                answer[i][j]+=arr1[i][k]*arr2[k][j]
            # b.append(a)
            # print(b)
        # answer.append(b)
    return answer
print(solution([[2, 3, 2], [4, 2, 4], [3, 1, 4]],[[5, 4], [2, 4],[3, 1]]))