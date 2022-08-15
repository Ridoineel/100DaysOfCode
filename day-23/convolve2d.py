#! /usr/bin/env python

def convolve2d(A, M):
	""" 2D convolution 
		A * M = B

	"""

	# adjust M with 0 
	# if her size is even 
	# and reverse it 
	M = prepareMask(M)

	ah, aw = len(A), len(A[0])
	mh, mw = len(M), len(M[0])
	B = [[0]*aw for _ in range(ah)]

	for i in range(ah):
		for j in range(aw):
			# square sub matrix of A 
			# with center = (oi, oj)
			S = submatrix(A, i, j, mw)

			for a in range(mh):
				for b in range(mw):
					B[i][j] += M[a][b] * S[a][b]
			
	return B


def submatrix(A, oi, oj, size):
	""" square sub matrix of A 
		with center = (oi, oj)

	"""

	ah, aw = len(A), len(A[0])
	S = []

	# add zeros list line(s) to top of S
	if oi <= size//2 - 1:
		S = [[0]*size for _ in range(size//2 - oi)]

	for k in range(max(oi - size//2, 0), min(oi + size//2 + 1, ah)): 
		next_line = []
		for p in range(max(oj - size//2, 0), min(oj + size//2 + 1, aw)):
			next_line.append(A[k][p])

		# add zeros to left of next_line
		if oj <= size//2 - 1:
			next_line = [0]*(size//2 - oj) + next_line

		# add zeros to right of next_line
		if oj > aw - size//2 - 1:
			next_line += [0]*(oj - aw + size//2 + 1)

		S.append(next_line)

	# add zeros list line(s) to bottom of S
	if oi > ah - size//2 - 1:
		S += [[0]*size for _ in range(oi - ah + size//2 + 1)]

	return S

def prepareMask(M):
	""" adjust M with 0 if size if even 
		and reverse it 

	"""

	mh, mw = len(M), len(M[0])

	## adjust with 0 if size if even
	if mh % 2 == 0:
		M = [[0]*mw] + M
		mh += 1
	
	if mw % 2 == 0:
		mw += 1
		for i in range(mh):
			M[i] = [0] + M[i]

	# now, mh = mw

	## reverse M

	# center of M
	mo = (mh//2, mw//2)

	for i in range(mh - 1):
		for j in range(mw - i):
			p = (i, j)
			# p image according to symmetry of center=mo
			p_opp = (2*mo[0] - i, 2*mo[1] - j)

			M[i][j], M[p_opp[0]][p_opp[1]] = M[p_opp[0]][p_opp[1]], M[i][j] 
	
	return M

def main():
	A = [
		[2, 1, 3, 0],
		[1, 1, 0, 5],
		[3, 3, 1, 0],
		[2, 0, 0, 2]
	]

	M = [
		[1, 0, 2],
		[2, 1, 0],
		[1, 0, 3]
	]

	B = convolve2d(A, M)

	print(*B, sep="\n")
if __name__ == '__main__':
	main()