import lab02

if __name__ == "__main__":
	lab02.initialize()

	# testing addition
	lab02.add(50)	
	lab02.subtract(20)
	if lab02.get_current_value() == 30:
		print("Test 1 passed")
	else:
		print("Test 1 failed")

	# testing multiplication and division
	lab02.subtract(lab02.get_current_value())
	lab02.add(20)
	lab02.multiply(5)
	lab02.divide(100)
	if lab02.get_current_value() == 1:
		print("Test 2 passed")
	else:
		print("Test 2 failed")

	# testing undo function
	lab02.subtract(lab02.get_current_value())
	lab02.add(5)
	lab02.multiply(2)
	lab02.undo()
	if lab02.get_current_value() == 5:
		print("Test 3 passed")
	else:
		print("Test 3 failed")
	
	# testing memory functionality
	lab02.subtract(lab02.get_current_value())
	lab02.subtract(20)
	lab02.add(-5)
	lab02.store()
	lab02.add(20)
	lab02.divide(30)
	lab02.recall()
	if lab02.get_current_value() == -25:
		print("Test 4 passed")
	else:
		print("Test 4 failed")