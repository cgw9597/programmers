def solution(binomial):
    answer = 0
    sp_bin = ''.join(binomial).split(' ')
    if sp_bin[1] == "+":
        answer = int(sp_bin[0]) + int(sp_bin[2])
    elif sp_bin[1] == "*":
        answer = int(sp_bin[0]) * int(sp_bin[2])
    else:
        answer = int(sp_bin[0]) - int(sp_bin[2])
    return answer