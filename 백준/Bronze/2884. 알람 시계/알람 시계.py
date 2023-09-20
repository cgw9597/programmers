H,M = list(map(int,input().split()))
if H>0 and M >= 45:
    print(f"{H} {M-45}")
elif H==0 and M<45:
    print(f"23 {60+(M-45)}")
elif H==0 and M>=45:
    print(f"{H} {M-45}")
else:
    print(f"{H-1} {60-(45-M)}")