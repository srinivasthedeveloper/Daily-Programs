#Python type 1

input()
n,d=list(map(int,input().split())),{}
for i in set(n):d[n.count(i)]=i
print(d[sorted(d)[-2]])

'''
Python Type 2

n=int(input())
l=list(map(int,input().split()))
s=set(l)
c=[l.count(i) for i in s]
c.sort()
print(*set([i for i in l if l.count(i)==c[len(c)-2]]))

RUBY SOLN

gets.to_i
n=gets.split.map &:to_i
p n.uniq.select{|i|n.count(i)==n.uniq.map{|i|n.count(i)}.sort[-2]}[0]
'''