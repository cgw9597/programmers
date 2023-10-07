def solution(s):
    li = ''.join(s).split()
    result = f"{min(list(map(int,li)))} {max(list(map(int,li)))}"
    return result