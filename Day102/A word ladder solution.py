I=input
l=[I()for i in '.'*int(I())]
f=1 if(len(l)>1 and len(set(l))==len(l))else 0
for i in range(1,len(l)):
    if(len(l[i-1])!=len(l[i]) or len(set(l[i-1]+l[i]))>=len(set(l[i]))):f=0;break
print(str(bool(f)).lower())