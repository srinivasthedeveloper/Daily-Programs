a,b=map(str,[input().strip() for i in range(2)])
print(*sorted(set(str("".join([i for i in a if i not in b]))+str("".join([i for i in b if i not in a])))))
'''
what it does is
l=[i for i in a if i not in b]
l.extend([i for i in b if i not in a])
print(*sorted(set(l)))
'''
