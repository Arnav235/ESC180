## Learning goals
# * Write simple functions
# * Pass information to a function via parameters
# * Pass information to a function via global variables
# * Return information from functions via return values and global variables
# * Use global variables as "static" information

def display_current_value():
    '''Display the current value

    '''
    print('Current value:', current_value)

def save_value():
    '''Save the current value for furture use

    '''

    global prev_value
    prev_value = current_value

def add(to_add):
    '''Add to_add to the current value
    Arguments:
    to_add: an integer to add to the current value

    '''

    global current_value
    save_value()
    if current_value != "ERROR":
        current_value += to_add

def subtract(to_subtract):
    '''Subtract to_subtract from the current value

    '''

    global current_value
    save_value()
    if current_value != "ERROR":
        current_value -= to_subtract

def multiply(to_mult):
    '''Multiply the current value by to_mult

    '''

    global current_value
    save_value()
    if current_value != "ERROR":
        current_value *= to_mult

def divide(to_divide):
    '''Divide the current value by to_divide if to_divide != 0, set the current
    value to 'ERROR' otherwise

    '''

    global current_value
    save_value()
    if current_value != "ERROR":
        if to_divide == 0:
            current_value = 'ERROR'
        else:
            current_value /= to_divide

def store():
    '''Emulate the memory button by storing the current value for future use
    Note: cannot be undone with the undo() button
    '''
    global mem_value
    mem_value = current_value

def recall():
    '''Emulate the recall button by retriving a stored memory value

    '''
    global current_value
    current_value = mem_value

def undo():
    '''Make the current value have the value it had before the last operation

    '''
    global current_value, prev_value
    current_value, prev_value = prev_value, current_value



def initialize():
    global current_value, prev_value, mem_value
    current_value = 0
    prev_value = 0
    mem_value = 0

def get_current_value():
	return current_value