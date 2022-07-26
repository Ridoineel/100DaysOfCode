"""
	Natural gradient descent algorithm
	on 2-dimensionnal point prediction

"""

import numpy as np


def cost(X, Y, a, b):
	return np.sum((Y - (a*X + b))**2)

def gradients(X, Y, a, b):
	gradEa = np.sum(-2*X*(Y - (a*X + b)))
	gradEb = np.sum(-2*(Y - (a*X + b)))
	
	return gradEa, gradEb
	
def predict(X, a, b):
	return a*X + b
	
def main():
	# the new value is predicted
	# according to this X and Y
	X = np.array([4, 7, 8, 10, 12])
	Y = np.array([1, 3, 3, 6, 7])

	# learning rate and epochs number
	δ = 0.001
	n = 1000
	
	# initial value of a and b
	a = 0
	b = 0
	
	loss = []
	
	for i in range(n):
		gradEa, gradEb = gradients(X, Y, a, b)
		
		loss.append(cost(X, Y, a, b))
		
		a = a - δ*gradEa
		b = b - δ*gradEb
	
	print("Learning finished...")
	print(f"f(x) = {a}x + {b}")
	print()
	
	while 1:
		x = float(input("x: "))
		
		print("predicted value:", predict(np.array([x]), a, b))

if __name__ == "__main__":
	main()
