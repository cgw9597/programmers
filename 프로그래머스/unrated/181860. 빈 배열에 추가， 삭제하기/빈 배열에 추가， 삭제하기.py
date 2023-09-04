def solution(arr, flag):
    answer = []
    for i,j in zip(arr,flag):
        if j:
            answer+=str(i)*i*2
        else:
            del answer[-i:]
    
    return [int(x) for x in answer]