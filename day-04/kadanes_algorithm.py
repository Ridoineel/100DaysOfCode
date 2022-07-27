
def max_sub_array(array):

	""" largest sum contiguous subarray

		using kadane's algorithm

	"""

	max_sum = float("-inf")
	current_sum = 0

	current_sublist = []
	ending_sublist = []

	for i in array:
		current_sum += i
		current_sublist += [i]

		if current_sum > max_sum:
			max_sum = current_sum
			ending_sublist = current_sublist.copy()
		

		if current_sum < 0:
			current_sum = 0
			current_sublist = []

	return max_sum, current_sublist

def main():
	L1 = [-1, 2, -1, 4, 5]
	L2 = [-2, -3, 4, -1, -2, 1, 5, -3]

	print(max_sub_array(L1)) # (10, [2, -1, 4, 5])
	print(max_sub_array(L2)) # (7, [4, -1, -2, 1, 5, -3])

if __name__ == "__main__":
	main()