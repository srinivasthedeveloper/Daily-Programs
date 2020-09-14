firstRow="qwertyuiop"
secondRow="asdfghjkl"
thirdRow="zxcvbnm"
flag=1
List=list(map(str,input().split(',')))
for i in List:
        f=sum([1 for _ in i.lower() if _ in firstRow])
        s=sum([1 for _ in i.lower() if _ in secondRow])
        t=sum([1 for _ in i.lower() if _ in thirdRow])
        if(f==len(i) or s==len(i) or t==len(i)):
                print(i,end=" ")
                flag=0
print("-1")if(flag)else print("",end="")
