def solution(absolutes, signs):
    answer = 0
    for ab,si in zip(absolutes, signs):
        if si:
            answer+=ab
        else:
            answer-=ab
    return answer



# def solution(absolutes, signs):
#     answer = 0
#     for i in range(len(absolutes)):
#         if signs[i] ==True:
#             answer+=absolutes[i]
#         else:
#             answer-=absolutes[i]
#     return answer