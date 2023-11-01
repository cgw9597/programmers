def solution(rank, attendance):
    answer = 0
    li = []
    stu = sorted([(r,i) for i,r in enumerate(rank)])
    for r,i in stu:
        if attendance[i]:
            li.append(i)
            if len(li) == 3:
                break
    answer = 10000*li[0] + 100*li[1] + li[2]
    return answer
