def solution(score):
    avg = []
    answer = []
    for eng, mat in score:
        avg.append((eng+mat)/2)
    avg_li = sorted(avg, reverse=True)
    for i in avg:
        answer.append(avg_li.index(i)+1)
    return answer