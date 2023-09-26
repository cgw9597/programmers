# def solution(left, right):
#     result = 0
#     my=list(range(left,right+1))
#     li=[]
#     for i in range(left, right+1):
#         answer = 0
#         for j in range(1,i+1):
#             if i%j==0:
#                 answer+=1
#         li.append(answer)
#     for idx,num in enumerate(li):
#         if num%2==0:
#             result+=my[idx]
#         else:
#             result-=my[idx]
#     return result
def solution(left, right):
    answer = 0
    from math import sqrt
    for i in range(left, right+1):
        if int(sqrt(i)) == sqrt(i):  # 제곱근이 정수면 약수개수 홀수다
            answer-=i
        else:
            answer+=i
    return answer