def solution(arr, queries):
    answer = []
    li=[]
    for s,e,k in queries:
        li = list(filter(lambda i:i>k, sorted(arr[s:e+1])))
        if len(li) > 0:
            answer.append(li[0])
        else:
            answer.append(-1)
    return answer