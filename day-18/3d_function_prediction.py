import numpy as np
import matplotlib.pyplot as plt
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense

f = lambda x, y: x*np.cos(y)

def main():
	# data
	# (x, y) in [a, b]^2
	a, b = -4, 4
	# points per grid
	n = 25 

	X = np.linspace(a, b, n)
	Y = np.linspace(a, b, n)

	XX, YY = np.meshgrid(X, Y)
	ZZ = f(XX, YY)

	INPUT = np.append(XX.reshape(-1, 1), YY.reshape(-1, 1), axis=1)
	OUTPUT = ZZ.reshape(-1, 1)

	# model
	p=10
	model = Sequential()
	model.add(Dense(p, input_dim=2, activation="relu"))
	model.add(Dense(p, activation="relu"))
	model.add(Dense(p, activation="relu"))
	model.add(Dense(1, activation="linear"))

	# model configuration
	model.compile(loss="mean_squared_error", optimizer="sgd")

	# training
	epochs = 1000

	for i in range(epochs):
		loss = model.train_on_batch(INPUT, OUTPUT)
		print(f"Loss {i}: {loss}")

	# Evaluation
	ZZ_predict = model.predict(INPUT).reshape(ZZ.shape)

	axe = plt.axes(projection="3d")
	axe.plot_surface(XX, YY, ZZ, color="red", alpha=0.7)
	axe.plot_surface(XX, YY, ZZ_predict, color="blue", alpha=0.7)

	plt.show()

if __name__ == "__main__":
	main()