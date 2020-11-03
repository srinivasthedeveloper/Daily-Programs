string1,string2,string3=map(str,input().split())
for upto in range(len(string1),0,-1):
        for start in range(len(string1)-upto+1):
                substring=string1[start:start+upto]
                if substring in string1 and substring in string2 and substring in string3:
                        print(substring)
                        exit()
print("-1")

