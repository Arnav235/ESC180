import numpy as np

def print_matrix(m_lol):
	for i in range(len(m_lol)):
		print(m_lol[i])

def get_lead_ind(row):
	for i in range(len(row)):
		if row[i] != 0:
			return i
	return len(row)

def get_row_to_swap(M, start_i):
	left_most_0 = len(M) -1
	left_most_idx = start_i
	for i in range(start_i, len(M)):
		for j in range(len(M[i])):
			if j >= left_most_0:
				break
			if M[i][j] != 0:
				left_most_0 = j
				left_most_idx = i
	
	return left_most_idx

def add_rows_coefs(r1, c1, r2, c2):
	np_r1 = np.array(r1)
	np_r2 = np.array(r2)

	return (c1*np_r1 + c2*np_r2).tolist()

def eliminate(M, row_to_sub, best_lead_ind):
	for i in range(row_to_sub +1, len(M)):
		coef = M[i][best_lead_ind] / M[row_to_sub][best_lead_ind]
		M[i] = add_rows_coefs(M[i], 1, M[row_to_sub], -coef)

def forward_step(M):
	for i in range(len(M)):
		print("The matrix is currently:")
		print_matrix(M)
		print("Now looking at row {}".format(i))
		swap_row = get_row_to_swap(M, i)
		swap_lead_ind = get_lead_ind(M[swap_row])
		print("Swapping rows {} and {} so that the entry {} in the current row is non-zero".format(i, swap_row, swap_lead_ind))
		M[i], M[swap_row] = M[swap_row], M[i]
		print("Adding row {} to rows below it to eliminate coefficients in column {}".format(swap_lead_ind, swap_lead_ind))
		eliminate(M, i, swap_lead_ind)
	
def backward_step(M):
	print("Backward Step----------------")
	for i in range(len(M) -1, 0, -1):
		lead_ind = get_lead_ind(M[i])
		print("Adding row {} to rows above it to eliminate coefficients in column {}".format(i, lead_ind))
		M.reverse()
		eliminate(M, len(M) - 1 -i, lead_ind)
		M.reverse()
		print("The matrix is currently:")
		print_matrix(M)
	
	print("Now dividing each row by the leading coefficient")
	for i in range(len(M)):
		lead_num = M[i][ get_lead_ind(M[i]) ]
		M[i] = (np.array(M[i]) / lead_num).tolist()
	
	print("The matrix is currently:")
	print_matrix(M)

def solve(M, b):
	for i in range(len(M)):
		M[i].append(b[i])
	forward_step(M)
	backward_step(M)
	np_arr = np.array(M)
	return np_arr[:, -1].tolist()



M = [[  1,  -2,   3],
	[3, 10, 1],
 	[  1,   5,   3]]
x = [1, 20, 3]

print(solve(M, np.matmul(np.array(M), np.array(x) )))