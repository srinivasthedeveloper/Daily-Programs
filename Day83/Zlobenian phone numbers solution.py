u = input()
n=u.replace(' ','')
n=''.join([k for k in u if k>='0' and k<='9'])
n='0'+n[len(n)-11:]
print(n[0:3],n[3:6],n[6:9],n[9:12])
