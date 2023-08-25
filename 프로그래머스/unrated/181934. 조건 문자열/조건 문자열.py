def solution(ineq, eq, n, m):
    answer = int(eval(str(n) + ineq + eq.replace('!','')+str(m)))
    return answer

# def solution(ineq, eq, n, m):
#     answer = 0
#     if ineq == ">" and eq == "=" and n>=m:
#         answer = 1
#     elif ineq == "<" and eq == "=" and n<=m:
#         answer = 1
#     elif ineq == ">" and eq == "!" and n>m:
#         answer = 1
#     elif ineq == "<" and eq =="!" and n<m:
#         answer = 1
#     return answer