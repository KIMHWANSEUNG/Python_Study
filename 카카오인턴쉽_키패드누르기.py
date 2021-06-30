


def solution(numbers, hand):
    answer=''
    left=[1,4,7]
    right=[3,6,9]
    lhand='*'
    rhand='#'
    numbers_dict={1:(0,0),2:(0,1),3:(0,2),
                4:(1,0),5:(1,1),6:(1,2),
                7:(2,0),8:(2,1),9:(2,2),
                '*':(3,0),0:(3,1),'#':(3,2)}
    
    for number in numbers :
        if number in left:
            answer+='L'
            lhand=number
        elif number in right:
            answer+='R'
            rhand=number
        else:
            lhand_distance=abs(numbers_dict[number][0]-numbers_dict[lhand][0])+abs(numbers_dict[number][1]-numbers_dict[lhand][1])
            rhand_distance=abs(numbers_dict[number][0]-numbers_dict[rhand][0])+abs(numbers_dict[number][1]-numbers_dict[rhand][1])

            if lhand_distance<rhand_distance:
                answer+='L'
                lhand=number
            elif lhand_distance>rhand_distance:
                answer+='R'
                rhand=number
            else :
                if hand == 'right':
                    answer+='R'
                    rhand=number
                else:
                    answer+='L'
                    lhand=number           


    return answer

print(solution([1, 2, 3, 4, 5, 6, 7, 8, 9, 0], "right"))
    #결과는 "LLRLLRLLRL"
	







def solution2(numbers, hand):
    answer = ''
    key_dict = {1:(0,0),2:(0,1),3:(0,2),
                4:(1,0),5:(1,1),6:(1,2),
                7:(2,0),8:(2,1),9:(2,2),
                '*':(3,0),0:(3,1),'#':(3,2)}

    left = [1,4,7]
    right = [3,6,9]
    lhand = '*'
    rhand = '#'
    for i in numbers:
        if i in left:
            answer += 'L'
            lhand = i
        elif i in right:
            answer += 'R'
            rhand = i
        else:
            curPos = key_dict[i]
            lPos = key_dict[lhand]
            rPos = key_dict[rhand]
            print('rpos',rPos)
            ldist = abs(curPos[0]-lPos[0]) + abs(curPos[1]-lPos[1])
            rdist = abs(curPos[0]-rPos[0]) + abs(curPos[1]-rPos[1])
            
            if ldist < rdist:
                answer += 'L'
                lhand = i
            elif ldist > rdist:
                answer += 'R'
                rhand = i
            else:
                if hand == 'left':
                    answer += 'L'
                    lhand = i
                else:
                    answer += 'R'
                    rhand = i

    return answer


#print(solution2([1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5],"right"))