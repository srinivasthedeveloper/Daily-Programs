firstRow="`1234567890-="
secondRow="qwertyuiop"
thirdRow="asdfghjkl"
fourthRow="zxcvbnm"
flag=1
List=list(map(str,input().split(',')))
for i in List:
        f=sum([1 for _ in i.lower() if _ in firstRow])
        s=sum([1 for _ in i.lower() if _ in secondRow])
        t=sum([1 for _ in i.lower() if _ in thirdRow])
        fr=sum([1 for _ in i.lower() if _ in thirdRow])
        if(len(i)in[f,s,t,fr]):
                print(i,end=" ")
                flag=0
print("-1")if(flag)else print("",end="")
