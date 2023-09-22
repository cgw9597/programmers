def solution(strArr):
    li=[]
    li2=[]
    for i in strArr:
        li.append(len(i))
    for j in set(li):
        li2.append(li.count(j))
    return max(li2)