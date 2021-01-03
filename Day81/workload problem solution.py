n=int(input())
m=int(input())
t=[]
for i in range(n):
    l=list(map(str,input().split()))
    mean=eval("+".join(l))//m
    var=sum((int(i)-mean)**2 for i in l)
    t.append(var)
print(t.index(min(t))+1)