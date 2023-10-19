def solution(s):
    answer = [0,0]
    num=0
    while num != 1:
        answer[0]+=1
        num = s.count('1')
        answer[1]+=len(s)-num
        s = format(num,'b')
    return answer