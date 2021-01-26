n=int(input())
s=""
t=""
for _ in range(n):
    t+=input().strip()
t+=' '
c=1
for i in range(len(t)-1):
    if(t[i]!=t[i+1]):
        if(c>1):
            s+=str(c)
        s+=t[i]
        c=0
    c+=1
print("".join(s.split()))
