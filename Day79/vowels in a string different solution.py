q='uUoOiIEeAa'
for i in ' '*int(input()):
 w=[x for x in input()if x.upper() in q]
 print(max(w,default='NONE',key=lambda r:q.find(r)))
