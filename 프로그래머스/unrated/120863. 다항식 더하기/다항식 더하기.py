def solution(polynomial):
    number = 0
    x = 0
    for char in polynomial.split(" + "):
        if char.isnumeric():
            number += int(char)
        else:
            x += int(char[:-1] or "1")
    return " + ".join([
        *([f"{x if x > 1 else ''}x"] if x else []),
        *([f"{number}"] if number else []),])