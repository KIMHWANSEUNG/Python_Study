def solution(a, b):
    answer = sum(map(lambda i: a[i]*b[i],range(len(a))))
    return answer


print (solution([1,2,3],[-3,-1,0,1]))


print(True)