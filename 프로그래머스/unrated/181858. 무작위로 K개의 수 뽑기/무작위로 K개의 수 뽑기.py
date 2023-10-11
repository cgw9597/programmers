def solution(arr, k):
    answer = []
    li = []
    for i in arr:
        if i not in li:
            li.append(i)
    if len(li) > k:
        answer = li[:k]
    else:
        answer += li + [-1] * (k - len(li))
    return answer