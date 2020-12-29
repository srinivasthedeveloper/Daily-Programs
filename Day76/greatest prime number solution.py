n=int(input())
l=sorted([int(input()) for i in range(n)],reverse=True)
for i in l:
    f=1
    for j in range(2,i//2):
        if(i%j==0):
            f=0
            break
    if(f):
        print(i)
        exit()