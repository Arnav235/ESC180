def list1_start_with_list2(list1, list2):
	if len(list1) < len(list2):
		return False
	for i in range(len(list2)):
		if list1[i] != list2[i]:
			return False
	return True

def match_pattern(list1, list2):
	for i in range(len(list1)):

		if i > len(list1) - len(list2):
			return False

		for j in range(len(list2)):
			if list2[j] != list1[i + j]:
				break
			if j == len(list2) -1:
				return True

	return False

def repeats(list0):
	for i in range(1, len(list0)):
		if list0[i-1] == list0[i]:
			return True
	return False

def print_matrix(M):
	print(str(len(M)) + "x" + str(len(M[0])))

def mult_M_v(M, v):
	for i in range(len(M)):
		new_vec = [a * b for a,b in zip(M[i], v)]
		M[i] = sum(new_vec)
	return M

def matrix_multi(M1, M2):
	new_M2 = []
	for i in range(len(M2[0])):
		new_M2.append([a[i] for a in M2])

	new_M = []
	for i in range(len(M1)):
		new_M.append( mult_M_v(M1.copy(), new_M2[i]) )
	
	returned_M = []
	for i in range(len(new_M[0])):
		returned_M.append([ a[i] for a in new_M ])
	
	return returned_M

Mat1 = [[1, 3, 5], 
		[5, 6, 8]]
Mat2 = [[3, 4],
		[4, 6],
		[2, 6]]

print(matrix_multi(Mat2, Mat1))
