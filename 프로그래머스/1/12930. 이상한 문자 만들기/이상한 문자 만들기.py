def solution(s):
    answer = []
    s = s.split(' ')
    for i in s:
        li=[]
        for j in range(len(i)):
            if j%2==0:
                li.append(i[j].upper())
            else:
                li.append(i[j].lower())
        li=''.join(li)
        answer.append(li)
    answer = ' '.join(answer)
    return answer