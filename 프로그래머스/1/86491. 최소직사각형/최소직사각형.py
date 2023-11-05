def solution(sizes):
    answer = 0
    max_li = []
    min_li = []
    for i in sizes:
        max_li.append(max(i))
        min_li.append(min(i))
    return max(max_li) * max(min_li)