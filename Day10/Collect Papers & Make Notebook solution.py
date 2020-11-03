n=int(input())
f=list(map(int,input().split()))
s=list(map(int,input().split()))
flag='f'
for i in range(n):
        if(flag=='f'):
                print(f[i],end=" ")
                if((f[i]%2==0 and s[i]%2==0)or(f[i]%2==1 and s[i]%2==1)):
                        print(s[i],end=" ")
                        flag='s'
        else:
                print(s[i],end=" ")
                if((f[i]%2==0 and s[i]%2==0)or(f[i]%2==1 and s[i]%2==1)):
                        print(f[i],end=" ")
                        flag='f'
