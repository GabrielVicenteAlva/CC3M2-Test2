import param
import math
import functools

#Puntos
P = [(-3,0),(-1,4),(2,3),(4,1)]
n = 4
param.points(*zip(*P))

# Calcular polinomio
def a(i,t):
	# Productoria
	factors = ((t-k)/(i-k) for k in range(n) if k!=i)
	return functools.reduce(lambda x,y:x*y,factors)
def L(t):
	X,Y = zip(*P)
	return \
	sum(X[i]*a(i,t) for i in range(n)), \
	sum(Y[i]*a(i,t) for i in range(n))

param.param(L,0,n-1,100)

