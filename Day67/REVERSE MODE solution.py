n=int(input())
l=[]
for i in range(2):
    l.append(list(map(int,input().split())))
s=0
for i in range(n):
    t=1
    for j in range(2):
        t*=l[j][i]
    s+=t
print(s)