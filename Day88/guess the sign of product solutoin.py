#Python type 1
a, b = [int(i) for i in input().split()]
if a<=0 and b>=0:
    print(0)
elif a>0:
    print(1)
else:
    print([-1,1][(b-a+1)%2==0])


#Python type 2
a,b=map(int,input().split())
l=[str(i) for i in range(a,b)]
# t=a
# for i in range(t,b):
#     l.append(str(i))
if(l):
    l=eval("*".join(l))*b
    print(1)if(l>0)else print(0)if(l==0)else print(-1)
else:
    print(0)