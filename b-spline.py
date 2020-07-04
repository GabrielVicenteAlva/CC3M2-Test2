import param
import math

#Puntos
P = [(-1,0),(1,4),(3,-2),(4,3),(6,1)]
n = 5
k = 3
param.points(*zip(*P))

# Algoritmo de De Boore
def S(t):
	d_x,d_y = zip(*(P+[(0,0)]))
	a = int(t)
	for j in range(1,k+1):
		temp_x,temp_y = [0]*(n+1),[0]*(n+1)
		for i in range(a-3+j,a+1):
			a_ir = (t-i)/(k-j+1)
			temp_x[i] = (1-a_ir)*d_x[i-1] + a_ir*d_x[i]
			temp_y[i] = (1-a_ir)*d_y[i-1] + a_ir*d_y[i]
		d_x,d_y = temp_x,temp_y
	return d_x[a],d_y[a]

param.param(S,3.,5.,100)
