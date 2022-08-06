"""
	Digits recognition DL model
	using keras mnist datasets

	By RidoineEl

"""

import matplotlib.pyplot as plt
import numpy as np
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
from tensorflow.keras.datasets import mnist
from tensorflow.keras.utils import to_categorical

# data normalization 
def dataNormalize(X, Y):
	# 28x28 -> 28*28
	X = X.reshape(X.shape[0], X.shape[1]**2)
	# 0..255 -> 0..1
	X = X/255

	#Y: 2 -> [0, 0, 1, 0, 0, 0, 0, 0, 0, 0]
	#: 5 -> [0, 0, 0, 0, 0, 1, 0, 0, 0, 0]
	Y = to_categorical(Y, num_classes=10)

	return X, Y

def main():
	(x_train, y_train), (x_test, y_test) = mnist.load_data()

	x_train, y_train = dataNormalize(x_train, y_train)
	x_test, y_test = dataNormalize(x_test, y_test)

	N, data_length = x_train.shape[0], x_train.shape[1]

	# model
	p=8
	model = Sequential()

	model.add(Dense(p, input_dim=data_length, activation="sigmoid"))
	model.add(Dense(p, activation="sigmoid"))
	model.add(Dense(10, activation="softmax"))

	# training
	model.compile(loss="categorical_crossentropy", optimizer="sgd", metrics=["accuracy"])
	model.fit(x_train, y_train, batch_size=32, epochs=70)

	# test
	Y_predict = model.predict(x_test)

	i=6
	print(Y_predict[i])
	print(np.argmax(Y_predict[i]))

	# show test result
	plt.imshow(x_test[6].reshape(28, 28))
	plt.show()

if __name__ == "__main__":
	main()

