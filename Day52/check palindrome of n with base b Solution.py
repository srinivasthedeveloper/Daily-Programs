import numpy
I=input
n=int(I())
b=int(I())
p=numpy.base_repr(n,base=b)
I(p==p[::-1])