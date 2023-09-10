def solution(emergency):
    answer = []
    li = sorted(emergency,reverse=True)
    for i in emergency:
        answer.append(li.index(i)+1)
        
    return answer