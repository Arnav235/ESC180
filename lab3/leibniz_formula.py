def approximate_pi():
	sum = 0
	for i in range (1000):
		sum += ((-1)**i) / (2*i + 1)
	return sum*4
	
print(approximate_pi())