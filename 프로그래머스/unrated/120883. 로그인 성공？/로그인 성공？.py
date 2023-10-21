def solution(id_pw, db):
    answer = ''
    for a,b in db:
        if id_pw[0] == a and id_pw[1] == b:
            return "login"
    for a,b in db:
        if id_pw[0] == a:
            return "wrong pw"
        else:
            answer = "fail"
    return answer