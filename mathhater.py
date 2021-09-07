import os
os.system('cls')
import numpy as np
def solution(answers):
    a = [1,2,3,4,5]
    b = [2,1,2,3,2,4,2,5]
    c = [3,3,1,1,2,2,4,4,5,5]
    answer = list([i,0] for i in range(1,4))

    for i in range(len(answers)) :
        if answers[i] == a[i%5] :
            answer[0][1] += 1
        if answers[i] == b[i%8] :
            answer[1][1] += 1
        if answers[i] == c[i%10] :
            answer[2][1] += 1
    answer.sort(key = lambda x : x[1], reverse=True)

    for i in range(1,3) :
        if answer[i][1] != answer[0][1] :
            answer = answer[:i]
            break

    return list(map(lambda x : x[0], answer))

print(solution([1,2,3,4,5]))
print(solution([1,3,2,4,2]))
print(solution([1,3,2,4,2,3,2,4,2,3,2,4,2,3,2,4,2,3,2,4,2,3,2,4,2]))