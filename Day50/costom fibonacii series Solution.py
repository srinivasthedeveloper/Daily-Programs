n=int(input())
n1=int(input())
n2=int(input())
print(n1)
print(n2)
for i in range(n-2):
    t=n1+n2
    n1=n2
    n2=t
    print(t)
