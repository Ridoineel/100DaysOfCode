
import numpy as np
import matplotlib.pyplot as plt
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
from tensorflow.keras.utils import to_categorical
from tensorflow.keras import optimizers

f = lambda x: np.cos(2*x) + x*np.sin(3*x) + x**0.5 - 2

def main():
	# data
	a , b, N = 0, 5, 100
	X = np.linspace(0, 5, 100)
	Y = f(X)
	
	X_train = X.reshape(-1, 1)
	Y_train = X.reshape(-1, 1)

	# model
	p = 10
	model = Sequential()
	model.add(Dense(p, input_dim=1, activation="tanh"))
	model.add(Dense(p, activation="tanh"))
	model.add(Dense(p, activation="tanh"))
	model.add(Dense(p, activation="tanh"))
	model.add(Dense(1, activation="linear"))

	# model configuration
	model.compile(loss="mean_squared_error", optimizer="adam", metrics=["accuracy"])

	# training
	history = model.fit(X_train, Y_train, batch_size=N, epochs=2000)

	# prediction
	Y_predict = model.predict(X_train)

	plt.plot(X_train, Y_train, c="blue", label="reference function")
	plt.plot(X_train, Y_predict, c="green", label="predicted")
	plt.legend()
	plt.show()

if __name__ == "__main__":
	main()