def solution(numbers, k):
    answer = 0
    numbers=numbers*k
    li=[]
    for i in range(k):
        li+=numbers[::2]
    return li[k-1]