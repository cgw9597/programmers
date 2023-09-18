# def solution(n):
#     result =  ""
#     for i in range(n):
#         li = ["수","박"] * n
#         result += li[i]
#     return result

def solution(n):
    return "수박" * (n//2) + "수" * (n%2)