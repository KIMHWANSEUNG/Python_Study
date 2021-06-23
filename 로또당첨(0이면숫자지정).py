def solution(lottos, win_nums):
    result = []
    max_answer = []
    min_answer = []
    for i in range(0,len(lottos)):
        if lottos[i] == 0 :
           max_answer.append(0);
        for j in range(0,len(win_nums)):
            if lottos[i] == win_nums[j]:
                 min_answer.append(lottos[i])
                 max_answer.append(lottos[i])

    result.append(7-len(max_answer))
    result.append(7-len(min_answer))

    if result[0] == 7 and result[1] == 7 :
             result[0]=6
             result[1]=6
    elif result[1] == 7:
        result[1] = 6        
       
    return result

print(solution([1, 1,1, 1, 1, 1],[38, 19, 20, 40, 15, 25]))
print(solution([1, 1,1, 1, 1, 1],[38, 19, 20, 40, 15, 25]))


##프로그래머스 답안

def solution2(lottos, win_nums):

    rank=[6,6,5,4,3,2,1]

    cnt_0 = lottos.count(0)
    ans = 0
    for x in win_nums:
        if x in lottos:
            ans += 1
    return rank[cnt_0 + ans],rank[ans]
