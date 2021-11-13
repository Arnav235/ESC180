def sum_of_cubes(n):
	sum = 0
	for i in range(1, n+1):
		sum += i ** 3
	return sum

def sum_of_cubes_formula(n):
	sum = 0
	for i in range(1, n+1):
		sum += i
	return sum ** 2

def check_sum(n):
	sum = sum_of_cubes(n)
	sum_formula = sum_of_cubes_formula(n)
	return sum == sum_formula

def check_sums_up_to_n(N):
	for i in range(1, N+1):
		if not check_sum(i):
			return False
	return True