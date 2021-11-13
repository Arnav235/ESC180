def count_evens(L):
	count = 0
	for i in L:
		if i % 2 ==0:
			count +=1
	return count

def list_to_str(lis):
	st = "["
	for i in lis:
		st += str(i) + ","
	st = st[:-1]
	return st+"]"


def lists_are_the_same(list1, list2):
	if len(list1) != len(list2): return False
	for i in range(len(list1)):
		if list1[i] != list2[i]:
			return False
	return True

def simplify_fraction(n, m):
	for i in range(max(n,m), 0, -1):
		if n%i ==0 and m%i == 0:
			n //= i
			m //= i
	print(n, "/", m)

import math

def num_sig_figs_pi_agrees(num_sig_figs):
	sum = 0
	i = 0
	while True:
		sum += ((-1)**i) / (2*i + 1)
		if int(sum*4*(10**(num_sig_figs-1))) == int(math.pi*(10**(num_sig_figs-1))):
			return i+1
		i += 1

def euclid_algo(a,b):
	if a % b == 0: return b
	if b % a == 0: return a
	r = a % b
	return euclid_algo(b,r)