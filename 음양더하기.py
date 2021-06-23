def solution(absolutes, signs):
    answer=0
    for i in range(0,len(absolutes)):
        if signs[i] == True:
            answer+=absolutes[i]
        elif signs[i] == False :
            answer-= absolutes[i]
    return answer

print(solution([4,7,12],[True,False,True])) # 예상값: 9