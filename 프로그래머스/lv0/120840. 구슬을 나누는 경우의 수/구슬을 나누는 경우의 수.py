def solution(balls, share):
    from math import factorial as fac
    return fac(balls)/(fac(balls-share)*fac(share))
                                            
                                            
# import math
# def solution(balls, share):
#     return math.comb(balls, share)                                