def solution(s):
    answer = 0
    x = s.split()
    for i in range(len(x)):
        if x[i]!="Z" and int(x[i]):
            answer+=int(x[i])
        elif x[i]=='Z':
            answer-=int(x[i-1])
    return answer