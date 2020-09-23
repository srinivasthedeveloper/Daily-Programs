a=input().split()[::-1]
print(input().split()[eval('%'.join(a))-1])#[n1,n2,...,nn][(a[0]%a[1])-1]
'''
n,p=map(int,input().split())
l=list(map(str,input().split()))
print(l[(p%n)-1])
'''
