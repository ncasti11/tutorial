# --------------------------------------------------------
#           PYTHON PROGRAM
# Here is where we are going to define our set of...
# - Imports
# - Global Variables
# - Functions
# ...to achieve the functionality required.
# When executing > python 'this_file'.py in a terminal,
# the Python interpreter will load our program,
# but it will execute nothing yet.
# --------------------------------------------------------

import math
import sys

# ------------------------------------------
#
# FUNCTION my_function2
#
# ------------------------------------------
def my_function2(a):
	res = math.sqrt(a)
	return res

# ------------------------------------------
#
# FUNCTION my_function1
#
# ------------------------------------------
def my_function1(a, b):
	result = a ** b
    return result

# ---------------------------------------------------------------
#           PYTHON EXECUTION
# This is the main entry point to the execution of our program.
# It provides a call to the 'main function' defined in our
# Python program, making the Python interpreter to trigger
# its execution.
# ---------------------------------------------------------------
if __name__ == '__main__':
	
	x = sys.argv[1]
	y = sys.argv[2]
	
	res = my_function1(x,y)
	print(res)
	
	res = my_function2(x)
	print(res)

