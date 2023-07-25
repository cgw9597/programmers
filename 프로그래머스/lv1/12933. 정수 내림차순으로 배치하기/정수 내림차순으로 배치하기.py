def solution(n):
    a_n = list(map(int,str(n)))
    a_n.sort(reverse=True)
    answer = int("".join(map(str,a_n)))
    return answer

# def solution(n):
#     n = int(n)
#     temp = map(str, str(n))
#     return int(''.join(sorted(temp, reverse = True)))