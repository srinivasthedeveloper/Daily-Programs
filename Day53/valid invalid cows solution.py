n=int(input())
s=list(input())
for i in range(n):
    t=list(input())
    f=1
    for j in range(len(t)):
        if(t[j]==s[j]):
            print("Invalid")
            f=0
            break
    if(f):print("Valid")