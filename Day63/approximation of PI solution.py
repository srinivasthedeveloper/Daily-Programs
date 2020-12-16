n=int(input())
print(sum(1 for _ in range(n) if 1>sum([float(x)**2 for x in input().split()]))/n*4)