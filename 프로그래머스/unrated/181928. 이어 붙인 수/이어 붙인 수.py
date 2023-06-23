def solution(num_list):
    a=[]
    b=[]
    for i in num_list:
        if i%2==0:
            a.append(i)
        else:
            b.append(i)
    a_=''.join(map(str,a))
    b_=''.join(map(str,b))
    answer = int(a_) + int(b_)
    return answer