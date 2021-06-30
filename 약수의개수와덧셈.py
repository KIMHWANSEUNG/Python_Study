def solution(left,right):
    answer = 0
    yaksu_count=[]
    for idx,i in enumerate(range(left,right+1)):
        count=0
        for j in range(1,i+1):
            if i%j==0:
                count+=1
        yaksu_count.append(count)
    print(yaksu_count)

    for i in yaksu_count:
        if i%2==0 :
            
            

    return answer
    
print(solution(13,17))