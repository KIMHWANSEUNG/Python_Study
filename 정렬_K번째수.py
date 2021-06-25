def solution(array, commands):
    answer = []
    for i in commands:
        a,b,c = i
        print(a,b,c)
        answer.append(list(sorted(array[a-1:b]))[c-1])
    
    return answer
    


print(solution([1, 5, 2, 6, 3, 7, 4],[[2, 5, 3], [4, 4, 1], [1, 7, 3]]))
#결과값
# array	                       commands	                       return
# [1, 5, 2, 6, 3, 7, 4]	[[2, 5, 3], [4, 4, 1], [1, 7, 3]]	[5, 6, 3]
#command에 인자를 뽑는다


#프로그래머스 답지 
def solution(array, commands):
    answer = []
    for command in commands:
        i,j,k = command
        answer.append(list(sorted(array[i-1:j]))[k-1])
    return answer