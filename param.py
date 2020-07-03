import matplotlib.pyplot as plt

# Figura
fig = plt.figure().gca()

# Dibujar punto
def points(x,y):
	fig.scatter(x, y)
	
# Rango
def linespace(mn,mx,n):
	step = float(mx-mn)/n
	while(mn<mx):
		yield mn
		mn += step
	yield mx

# Dibujar ecuacion parametrica
def param(f,mn,mx,seg=100):
	fig.plot(*zip(*(f(t) for t in linespace(mn,mx,seg))))
	plt.show()

# Ejemplo
if __name__=='__main__':
	param(lambda t:(t,t*t),0,1,100)
