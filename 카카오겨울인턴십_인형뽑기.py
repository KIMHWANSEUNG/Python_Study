def solution(board, moves):
    stack_list = []
    pop_count = 0
    
    for i in moves:
        for j in range(len(board)):
            if board[j][i-1] != 0 :
                stack_list.append(board[j][i-1])
                board[j][i-1]=0

                if len(stack_list) >1:
                    if stack_list[-1] == stack_list[-2]:
                        stack_list.pop(-1)
                        stack_list.pop(-1)
                        pop_count+=2
                break
        
    return pop_count




print(solution([[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]],[1,5,3,5,1,2,1,4]))











#01130302 입력 , 0은 빈칸
#11332 출력 => 4개가 터짐 
# 2

def solution2(board, moves):
    stacklist = []
    answer = 0

    for i in moves:
        for j in range(len(board)):
            if board[j][i-1] != 0:
                stacklist.append(board[j][i-1])
                board[j][i-1] = 0
        
                if len(stacklist) > 1:
                    if stacklist[-1] == stacklist[-2]:
                        stacklist.pop(-1)
                        stacklist.pop(-1)
                        answer += 2     
                break
    print(stacklist)
    return answer

#print(solution2([[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]],[1,5,3,5,1,2,1,4]))


#처음에 잘못 푼 코드

# def solution(board, moves):
#     board_list = list()
#     pop_count = 0
   
#     for seq in moves:
#         if board[seq-1][-1] == 0 :
#             continue

#         board_list.append(board[seq-1][-1])
#         board[seq-1].pop(-1)
#         if len(board_list)>1:
#             if board_list[-1] == board_list[-2]:
#                 board_list.pop(-1)
#                 board_list.pop(-1)
#                 pop_count+=2
        
#     print(board_list)
        
#     return pop_count
