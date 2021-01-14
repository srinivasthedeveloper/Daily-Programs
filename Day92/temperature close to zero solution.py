n=int(input())
l=list(map(int,input().split()))
t=[abs(i) for i in l]
#print(t)
if(min(t)in l):
    print(min(t))
else:
    print(-min(t))