import numpy as np
import matplotlib.pyplot as plt

def convProdSubLists(_list, motf_length):
	ln = len(_list)
	mn = motf_length
	mid_m = mn//2

	for i in range(ln):
		# number of elements in sub list
		# at left and right of _list[i]
		sub_list_nb_right = mid_m
		sub_list_nb_left = mn - mid_m - 1

		index_first = i - sub_list_nb_left
		index_last = i + sub_list_nb_right + 1

		# sub list with size=mn
		sub_list = _list[max(0, index_first):index_last]

		# zeros to add if sub list length 
		# not equal to mn
		zeros_to_add = [0]*(mn - len(sub_list))

		if index_last > ln:
			sub_list += zeros_to_add

		if index_first < 0: 
			sub_list = zeros_to_add + sub_list


		yield sub_list


def convProd(_list, motf):
	ln = len(_list)
	mn = len(motf)
	mid_m = mn//2

	new_list = []

	for sub_list in convProdSubLists(_list, mn):
		# reverse motf
		# don't use motf.reverse() or
		# motf[::-1] because of speed performance
		motf_reversed = reversed(motf)

		new_value = sum(a*b for a,b in zip(sub_list, motf_reversed))

		new_list.append(new_value)


	return new_list

def drawPoints(points_1, points_2):
	X1 = range(len(points_1))
	X2 = range(len(points_2))

	plt.plot(X1, points_1, label="Points 01")
	plt.plot(X2, points_2, label="Points 02")

	plt.grid()
	plt.legend()

	plt.show()

def main():
	L = [1, 0, 3, 5, 1]
	M = [1, 2, 3]

	# L = [4, 2, 1, 4, 5, 1, 3]
	# M = np.ones(3)/3

	# L = [4, 2, 1, 4, 5, 1, 3]
	# M = np.ones(5)/5
	
	new_L = convProd(L, M)



	print(L, "x", M, "=>", new_L)
	print(convProd(new_L, M))
	drawPoints(L, new_L)

if __name__ == '__main__':
	main()