import param

#Puntos
P = [(-3,0),(-1,4),(2,3),(4,1)]
n = 4
param.points(*zip(*P))

# Polinomio hallado en el examen
def B(t):
	return \
	-3 + 6*t + 3*t**2 - 2*t**3, \
	12*t - 15*t**2 + 4*t**3

param.param(B,0.,1.,100)
