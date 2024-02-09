def Derivative(f, a, h=0.00001):
	return (f(a + h) - f(a - h))/ (2 * h)
def Newton(f, a, h, maxiter):
	count = 1
	g = a
	while abs(round(f(g), 7)) != abs(round(a,75)):
		g = g - ((f(g) - a)/ Derivative(f, g, h))
		if count > maxiter:
			break
		count += 1
	return g
# Charles Truscott Watters. MITx MIT OCW

print(Newton(lambda x: x ** 2, 55, 0.0000001, 19551993))