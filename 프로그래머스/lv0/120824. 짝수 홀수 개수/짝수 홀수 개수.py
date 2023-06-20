def solution(num_list):
    x=[]
    y=[]
    for i in num_list:
        if i%2==0:
            x.append(i)
        else:
            y.append(i)
        answer = (len(x),len(y))
    return answer