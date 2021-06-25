def solution(answers):
    pattern1 = [1, 2, 3, 4, 5]
    pattern2 = [2, 1, 2, 3, 2, 4, 2, 5]
    pattern3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    score = [0,0,0]
    result = []
    for idx,answer in enumerate(answers):
        if answer == pattern1[idx%len(pattern1)] :
            score[0] += 1
        if answer == pattern2[idx%len(pattern2)] :
            score[1] += 1
        if answer == pattern3[idx%len(pattern3)] :
            score[2] += 1
        
    print('스코어:',score)
    
    for idx,val in enumerate(score):
        if val == max(score):
            result.append(idx+1)

    return result

print(solution([1,2,3,4,5]))









#프로그래머스 답안
def solution2(answers):
    pattern1 = [1,2,3,4,5]
    pattern2 = [2,1,2,3,2,4,2,5]
    pattern3 = [3,3,1,1,2,2,4,4,5,5]
    score = [0, 0, 0]
    result = []

#pattern1[idx%len(pattern1)] 이런식으로 쓴 이유는 패턴을 위해서 패턴의 크기만큼 걸어둘려도 

    for idx, answer in enumerate(answers):
        if answer == pattern1[idx%len(pattern1)]:
            score[0] += 1
        if answer == pattern2[idx%len(pattern2)]:
            score[1] += 1
        if answer == pattern3[idx%len(pattern3)]:
            score[2] += 1

    for idx, s in enumerate(score):
        if s == max(score):
            result.append(idx+1)

    return result

 #print(solution2([1,2,3,4,5]))