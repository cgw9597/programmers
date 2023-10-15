def solution(picture, k):
    result=[]
    answer = []
    for j in picture:
        result+=[j]*k
    for i in result:
        answer.append(i.replace('.','.'*k).replace('x','x'*k))
    return answer