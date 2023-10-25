def solution(chicken):
    answer = 0
    while chicken >= 10:
        eat = chicken//10
        answer += eat
        chicken = chicken%10 + eat
    return answer