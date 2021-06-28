def solution(numbers, hand):
    answer = []
    for i in numbers:
        if i in [1,4,7]:
            answer.append('L')
        elif i in [3,6,9]:
            answer.append('R')
        elif i in [2,5,8,0]:
            
           
    
    
        

    return answer

print(solution([1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5],"right"))
    #결과는 "LRLLLRLLRRL"